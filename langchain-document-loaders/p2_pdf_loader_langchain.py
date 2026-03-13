from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from dotenv import load_dotenv  
import json
load_dotenv()



def load_docs(_):
    current_dir = Path(__file__).parent
    file_path = current_dir / "network_ai_notes.pdf"
    loader = PyPDFLoader(str(file_path))
    return loader.load()
    


# Extract text from pages
def extract_text(docs):
    content = "\n\n".join([doc.page_content for doc in docs])
    return {"topic": content}

prompt = PromptTemplate(
    template="Summary the following topic: {topic} in 3 senetences",
    input_variables=["topic"]
)

model = ChatOpenRouter(
    model="google/gemma-3-12b-it",      
    temperature=0.7,
)

parser = StrOutputParser()


chain = RunnableLambda(load_docs) | RunnableLambda(extract_text) | prompt | model | parser

chain.get_graph().print_ascii()

result = chain.invoke({})

print(result)
