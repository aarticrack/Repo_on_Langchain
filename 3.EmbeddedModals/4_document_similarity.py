from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding= GoogleGenerativeAIEmbeddings(model='gemini-embedding-001', dimensions=300)
documents = [
     "Sachin Tendulkar: The unparalleled 'Master Blaster' who defined a generation of batting excellence.",
     "MS Dhoni: A cool-headed, tactical captain known for finishing matches with calm expertise.",
     "Virat Kohli: A modern-day batting machine with unmatched intensity and chase-master ability.",
     "Sir Don Bradman: The undisputed greatest batsman in history with a legendary average of 99.94.",
     "Brian Lara: A graceful left-hander capable of massive, match-winning scores.",
     "Ricky Ponting: A fierce competitor and dominant Australian captain. ",
]

query= "Tell me about MS Dhoni"
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores=cosine_similarity([query_embedding], doc_embeddings)[0]
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("Similarity score is : ",score)
