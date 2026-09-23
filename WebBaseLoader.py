from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_path="https://www.sap.com/india/products/financial-management.html?url_id=banner-in-homepage-row4-pos1-financial-management-260512")

data=loader.load()
print(data[0].page_content)