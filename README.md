## Data Framework
- [LLAMA INDEX](https://llamaindex.ai)

## Vectors Databases
- [CHROMA](https://docs.trychroma.com/)
- [WEAVIATE](https://weaviate.io/)

## Containers
- [WEAVIATE](https://weaviate.io/developers/weaviate/installation/docker-compose)

## Structure

.
├── chatbot_llama_index
│   ├── chroma_core.py
│   ├── chroma_generate.py
│   ├── data
│   │   ├── chroma
│   │   ├── DOC 1.pdf
│   │   ├── DOC 2.pdf
│   │   ├── DOC 3.pdf
│   │   ├── DOC 4.pdf
│   │   ├── DOC 5.pdf
│   ├── __init__.py
│   ├── main.py
│   ├── settings.py
│   ├── weaviate_core.py
│   └── weaviate_generate.py
├── docker
│   └── weaviate
│       └── docker-compose.yml
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py