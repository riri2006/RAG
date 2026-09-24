from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

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
