from langchain_community.document_loaders import TextLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

# embeddings = ChatOpenRouter(
#     model="mistralai/mistral-embed-2312"
# )

embeddings = OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    base_url="https://openrouter.ai/api/v1"
)


loader = TextLoader('langchain-text-splitters/semantic_splitter_test.txt')
docs = loader.load()
print(docs[0].page_content)

splitter = SemanticChunker(embeddings)

chunks = splitter.split_documents(docs)


print(chunks)

