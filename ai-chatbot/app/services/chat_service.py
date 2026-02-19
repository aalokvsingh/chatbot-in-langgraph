from app.graph.builder import build_graph
from langchain_core.messages import HumanMessage

class ChatService:

    def __init__(self):
        self.graph = build_graph()

    def chat(self, user_input: str):
        result = self.graph.invoke(
            {
                "messages": [HumanMessage(content=user_input)]
            }
        )
        return result["messages"][-1].content
