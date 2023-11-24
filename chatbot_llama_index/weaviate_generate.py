import logging
import sys
import os
import settings
import weaviate
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import WeaviateVectorStore
from llama_index.storage.storage_context import StorageContext

# Logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Env
os.environ["OPENAI_API_KEY"] = settings.OPENAI_KEY

# Connect with container local
resource_owner_config = weaviate.AuthApiKey("12345678")
client = weaviate.Client("http://localhost:8080", auth_client_secret=resource_owner_config)

# Load all documents
documents = SimpleDirectoryReader("./data").load_data()

vector_store = WeaviateVectorStore(weaviate_client=client, index_name="Vlms")
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create index
index = VectorStoreIndex.from_documents(documents=documents, storage_context=storage_context)