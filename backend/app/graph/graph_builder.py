from langgraph.graph import StateGraph, START, END

from app.graph.state import InsightBotState
from langgraph.checkpoint.memory import MemorySaver
def route_agent(state):

    selected_agent = state["selected_agent"]

    if selected_agent == "rag_agent":
        return "rag_agent"

    if selected_agent == "rag_then_tool":
        return "rag_then_tool"

    if selected_agent == "tool_agent":
        return "tool_agent"

    return "general_agent"

def route_after_rag(state):

    if state.get("selected_agent") == "rag_then_tool":
        return "handoff"

    return "end"

def route_approval(state):

    if state.get("approved") is True:
        return "execute_tool"

    return "rejected"


def build_graph(
    retrieve_node,
    prompt_node,
    llm_node,
    intent_node,
    general_llm_node,
    tool_node,
    approval_node,
    execute_tool_node,
    summarization_node,
    security_node,
    # Multi-Agent
    supervisor_node,
    general_agent_node,
    tool_agent_node,
    agent_handoff_node,
):

    builder = StateGraph(InsightBotState)

    # Register Nodes
    builder.add_node("intent", intent_node)
    builder.add_node("retrieve", retrieve_node)
    # Parallel nodes
    builder.add_node("summarization",summarization_node)
    builder.add_node("security",security_node,)

    builder.add_node("prompt", prompt_node)
    builder.add_node("llm", llm_node)
    builder.add_node("general_llm", general_llm_node)
    builder.add_node("tool", tool_node)
    builder.add_node("approval", approval_node)
    builder.add_node("execute_tool", execute_tool_node)
    builder.add_node(
        "supervisor",
        supervisor_node,
    )

    builder.add_node(
        "general_agent",
        general_agent_node,
    )

    builder.add_node(
        "tool_agent",
        tool_agent_node,
    )

    builder.add_node(
    "agent_handoff",
    agent_handoff_node,
                         )
    
    # Connect Nodes
    builder.add_edge(
        START,
        "supervisor",
    )
    # ------------------------------------------------
    # Intent Routing
    # ------------------------------------------------
    builder.add_conditional_edges(
        "supervisor",
        route_agent,
        {
            "rag_agent": "retrieve",
            "rag_then_tool": "retrieve",
            "tool_agent": "tool_agent",
            "general_agent": "general_agent",
        },
    )
    # ------------------------------------------------
    # DOCUMENT / RAG FLOW
    # ------------------------------------------------

    # Fan-out: run these two nodes in parallel
    builder.add_edge("retrieve","summarization")

    builder.add_edge("retrieve","security")
    
    # Fan-in: wait for both before PromptNode
    builder.add_edge("summarization","prompt")
    builder.add_edge("security","prompt")


    builder.add_edge("prompt", "llm")

    builder.add_conditional_edges(
    "llm",
    route_after_rag,
    {
        "handoff": "agent_handoff",
        "end": END,
    },
                                    ) # gneram document end chunk rag

    builder.add_edge(
    "agent_handoff",
    "tool_agent",
)
    # ------------------------------------------------
    # GENERAL LLM FLOW
    # ------------------------------------------------
    # builder.add_edge("general_llm", END)#genral llm end


    # ------------------------------------------------
    # TOOL / HITL FLOW
    # ------------------------------------------------

    # builder.add_edge("tool", "approval")#tool end
    builder.add_edge(
    "tool_agent",
    "approval",
                    )


    
    builder.add_conditional_edges(
    "approval",
    route_approval,
    {
        "execute_tool": "execute_tool",
        "rejected": END,
    },
                                )
    builder.add_edge("execute_tool", END)

    builder.add_edge(
    "general_agent",
    END,
                    )

    checkpointer = MemorySaver()
    return builder.compile(checkpointer=checkpointer)