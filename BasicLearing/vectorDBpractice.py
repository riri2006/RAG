from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

doc1=Document(
    page_content="Apple is a sweet and crunchy fruit. It is commonly red, green, or yellow and is a good source of fiber.",
    metadata={"fruit":"Apple"}
)