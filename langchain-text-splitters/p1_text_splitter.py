from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('langchain-text-splitters/network_ai_notes.pdf')
docs = loader.load()

splitter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    separator=''
    )
chunks=splitter.split_documents(docs)
import pprint
pprint.pprint(chunks[1])

