from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv

load_dotenv()

# Define the data model for the input string
class InputString(BaseModel):
    text: str

# Instantiate FastAPI
app = FastAPI()

prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)
output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")


chain = (
    {"topic": RunnablePassthrough()} 
    | prompt
    | model
    | output_parser
)

# Define the endpoint
@app.post("/llm_response")
async def get_llm_response(input_string: InputString):
    # Invoke the Langchain chain with the input string as the topic
    response = chain.invoke(input_string.text)
    
    # Return the response
    return  response
