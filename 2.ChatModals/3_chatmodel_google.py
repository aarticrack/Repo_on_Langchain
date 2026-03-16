from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("GOOGLE_API_KEY"))


model=ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite-preview')
response=model.invoke("what is LangChain?")
print(response.content)
