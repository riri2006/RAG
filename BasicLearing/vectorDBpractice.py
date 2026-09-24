from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from pprint import pprint

doc1=Document(
    page_content="This document consists of red apple",
    metadata={"fruit":"Apple"}
)

doc2=Document(
    page_content="This documents consists of yellow mango",
    metadata={"fruit":"Mango"}
)

doc3=Document(
    page_content="This document consists of pink lychee ",
    metadata={"fruit":"Lychee"}
)

docs=[doc1,doc2,doc3]

emebedding = OllamaEmbeddings(model="nomic-embed-text")

vdb=Chroma(
    embedding_function=emebedding,
    persist_directory="chroma_db",
    collection_name="Sampling"
)

vdb.add_documents(docs)
result=vdb.get(include=['embeddings','documents','metadatas'])
pprint(result)