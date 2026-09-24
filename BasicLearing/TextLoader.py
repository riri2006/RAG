#to check how the data are being stored and how the DOCUMENT works 
from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\riddh\OneDrive\Desktop\RV\RAG\sample.txt",encoding="utf-8")

data = loader.load()
print("\nLOAD:\n",data)

data1 = loader.lazy_load()
for doc in data1:
    print("\nLAZY LOAD:\n",doc.page_content)

# type of data
print("\nLOAD",type(data))
print("\nLAZY LOAD",type(data1))

#length 
print("\nLENGTH OF LOAD",len(data))

#data content and metadata
# print("\nPAGE CONTENT",data[0].page_content)
# print("\nMETADATA",data[0].metadata)


