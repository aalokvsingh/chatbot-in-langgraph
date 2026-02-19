from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage
from app.config import settings

llm = ChatGoogleGenerativeAI(
    model=settings.MODEL_NAME,
    google_api_key=settings.GOOGLE_API_KEY,
    temperature=0.3,
)

def llm_node(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
