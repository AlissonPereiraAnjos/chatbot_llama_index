import os
import settings
import chromadb
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext

os.environ["OPENAI_API_KEY"] = settings.OPENAI_KEY

# Initialize client
db = chromadb.PersistentClient(path="./data/chroma")

# Get collection
chroma_collection = db.get_or_create_collection("vlms")

# Assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create index
index = VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context)

# Methods
def execute_query(query:str):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response

def execute_query_streaming(query:str):
    query_engine = index.as_query_engine(streaming=True)
    response = query_engine.query(query)
    return response