from langchain_huggingface import HuggingFaceEmbeddings

Embedding=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')
text="Delhi is the Capital of India"
vector=Embedding.embed_query(text)
print(str(vector))
 