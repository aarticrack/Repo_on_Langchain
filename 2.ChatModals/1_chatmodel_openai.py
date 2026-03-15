from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model= ChatOpenAI(model='gpt-4', temperature=1.8, max_completion_tokens=10)
response=model.invoke("What is Langraph?")
print(response)
#here response will be with added additional keyword argument so to ignore that and to get only response use"response.content"
