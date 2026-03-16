from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding= OpenAIEmbeddings(model='text-embedding-3-large',dimensions=100)
documents=[
    "Delhi is the Capital of India"
    "kolkata is the Capital of WestBengal"
    "Paris is the Capital of France"
]

result=embedding.embed_documents(documents)
print(str(result))
