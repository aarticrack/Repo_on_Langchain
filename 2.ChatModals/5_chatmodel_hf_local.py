from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFacePipeline.from_model_id(
    model_id='HuggingFaceH4/zephyr-7b-beta',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.4,
        max_new_tokens=100
    )
    
)

model=ChatHuggingFace(llm=llm)
response=model.invoke("what is the capital of India?")
print(response.content)

    

