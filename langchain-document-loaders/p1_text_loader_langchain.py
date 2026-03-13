from langchain_community.document_loaders import TextLoader
from pathlib import Path
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import json
load_dotenv()

prompt = PromptTemplate(
    template="Summary the following topic: {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

model = ChatOpenRouter(
    model="google/gemma-3-12b-it",      
    temperature=0.7,
)




def load_docs(_):
    current_dir = Path(__file__).parent
    file_path = current_dir / "network_operations_manual.txt"
    loader = TextLoader(str(file_path), encoding="utf-8")
    return loader.load()

def extract_content(docs):
    return {"topic": docs[0].page_content}

# runnable1 = RunnableLambda(lambda x: x[0].page_content)  # Truncate the input to the first 1000 characters

chain = RunnableLambda(load_docs) | RunnableLambda(extract_content) | prompt | model | parser

chain.get_graph().print_ascii()


result = chain.invoke({})

print(result)