#to check how the data are being stored and how the DOCUMENT works 
from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\riddh\OneDrive\Desktop\RV\RAG\sample.txt",encoding="utf-8")
data = loader.load()

#type of data
print(type(data))

#length 
print("\nLENGTH",len(data))

#data content and metadata
print("\nPAGE CONTENT",data[0].page_content)
print("\nMETADATA",data[0].metadata)

