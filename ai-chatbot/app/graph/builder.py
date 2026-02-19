from langgraph.graph import StateGraph, START, END
from app.graph.state import ChatState
from app.graph.nodes.llm_node import llm_node

def build_graph():

    builder = StateGraph(ChatState)

    builder.add_node("llm", llm_node)

    builder.add_edge(START, "llm")
    builder.add_edge("llm", END)

    return builder.compile()
