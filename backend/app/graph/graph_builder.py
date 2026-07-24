from langgraph.graph import StateGraph, START, END

from app.graph.state import InsightBotState


def build_graph(
    retrieve_node,
    prompt_node,
    llm_node,
):

    builder = StateGraph(InsightBotState)

    # Register Nodes
    builder.add_node("retrieve", retrieve_node)
    builder.add_node("prompt", prompt_node)
    builder.add_node("llm", llm_node)

    # Connect Nodes
    builder.add_edge(START, "retrieve")
    builder.add_edge("retrieve", "prompt")
    builder.add_edge("prompt", "llm")
    builder.add_edge("llm", END)

    return builder.compile()