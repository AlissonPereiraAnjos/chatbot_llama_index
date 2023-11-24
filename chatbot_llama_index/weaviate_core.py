import logging
import sys
import os
import settings
import weaviate
from llama_index import VectorStoreIndex
from llama_index.vector_stores import WeaviateVectorStore

# Logging
# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Env
os.environ["OPENAI_API_KEY"] = settings.OPENAI_KEY

# Connect with container local
resource_owner_config = weaviate.AuthApiKey("12345678")
client = weaviate.Client("http://localhost:8080", auth_client_secret=resource_owner_config)

# Load Index
vector_store = WeaviateVectorStore(weaviate_client=client, index_name="Vlms")
index = VectorStoreIndex.from_vector_store(vector_store)

# Methods
def execute_query(query:str):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response

def execute_query_streaming(query:str):
    query_engine = index.as_query_engine(streaming=True)
    response = query_engine.query(query)
    return response

