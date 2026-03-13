from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('langchain-text-splitters/network_ai_notes.pdf')
docs = loader.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20
    )
chunks=splitter.split_documents(docs)
import pprint
print(len(chunks),'\n\n')

pprint.pprint(chunks)

