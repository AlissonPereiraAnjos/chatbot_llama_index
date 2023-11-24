import os
import settings
import chromadb
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext

os.environ["OPENAI_API_KEY"] = settings.OPENAI_KEY

# Load all documents
documents = SimpleDirectoryReader("./data").load_data()

# Initialize client, setting path to save data
db = chromadb.PersistentClient(path="./data/chroma")

# Create collection
chroma_collection = db.get_or_create_collection("vlms")

# Assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create index
index = VectorStoreIndex.from_documents(documents=documents, storage_context=storage_context)