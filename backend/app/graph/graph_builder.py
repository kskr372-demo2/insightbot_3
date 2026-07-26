from langgraph.graph import StateGraph, START, END

from app.graph.state import InsightBotState

def route_intent(state):

    if state["intent"] == "general":
        return "general"

    return "document"
def build_graph(
    retrieve_node,
    prompt_node,
    llm_node,
    intent_node,
    general_llm_node
):

    builder = StateGraph(InsightBotState)

    # Register Nodes
    builder.add_node("intent", intent_node)
    builder.add_node("retrieve", retrieve_node)
    builder.add_node("prompt", prompt_node)
    builder.add_node("llm", llm_node)
    builder.add_node("general_llm", general_llm_node)

    # Connect Nodes
    builder.add_edge(START, "intent")
    # builder.add_edge(START, "retrieve")
    builder.add_conditional_edges(
                                    "intent",
                                  route_intent,{
                            "document": "retrieve",
                            "general": "general_llm",
                                                },)
    builder.add_edge("retrieve", "prompt")
    builder.add_edge("prompt", "llm")
    builder.add_edge("llm", END)
    builder.add_edge("general_llm", END)

    return builder.compile()