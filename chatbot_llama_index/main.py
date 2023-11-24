import time

queries = [
    "What is VLMS?",
    "Can documents be added to a retired entity during the upcoming document migration?",
    "Removing the IOQ in the Framework will change the status to 'Validated'. Is there a way to correct the status to 'Validated'?",
    "the screenshot capture function is not working as intended during a test script. This issue has also been observed in lower environments, despite assurances from ValGenesis that it would work in PRD.",
    "Unable to update mapping for executable document GLO-AIP-CS-LD-00001.02-E-001.",
    "What are the modules of VLMS?",
    "How to log in in VLMS?"
]

# Chroma Response
import chroma_core

print("==CHROMA (local database)==")
for query in queries:
    start_time = time.perf_counter()
    response = chroma_core.execute_query(query)
    end_time = time.perf_counter()
    print("--------------------------------------------------------------")
    print(f"Query: {query}")
    print(f"Answer: {response}")
    print(f"Time: {end_time - start_time:0.4f} seconds")
    print("--------------------------------------------------------------")

# Weaviate Response
import weaviate_core

print("==WEAVIATE (container)==")
for query in queries:
    start_time = time.perf_counter()
    response = weaviate_core.execute_query_streaming(query)
    response.print_response_stream()
    end_time = time.perf_counter()
    print("--------------------------------------------------------------")
    print(f"Query: {query}")
    print(f"Answer: {response}")
    print(f"Time: {end_time - start_time:0.4f} seconds")
    print("--------------------------------------------------------------")
