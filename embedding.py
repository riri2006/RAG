from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector = embeddings.embed_query("Hello, how are you?")

print(vector)