from langchain_text_splitters import RecursiveCharacterTextSplitter,Language


Mycode = '''
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def load_docs(_):
    current_dir = Path(__file__).parent
    file_path = current_dir / "network_ai_notes.pdf"
    loader = PyPDFLoader(str(file_path))
    return loader.load()


def extract_text(docs):
    content = "\n\n".join([doc.page_content for doc in docs])
    return {"content": content}


prompt = PromptTemplate(
    template="Summarize the following content in 3 sentences:\n\n{content}",
    input_variables=["content"]
)

model = ChatOpenRouter(
    model="google/gemma-3-12b-it",
    temperature=0.7,
)

parser = StrOutputParser()

chain = (
    RunnableLambda(load_docs)
    | RunnableLambda(extract_text)
    | prompt
    | model
    | parser
)

chain.get_graph().print_ascii()

result = chain.invoke({})

print(result)
'''




splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=20
    )
chunks=splitter.split_text(Mycode)
import pprint
print(len(chunks),'\n\n')

pprint.pprint(chunks)

