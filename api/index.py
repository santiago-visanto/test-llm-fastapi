from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv

load_dotenv()

# Define the endpoint
@app.get("/api/llm_response")
async def get_llm_response():
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

    
    # Invoke the Langchain chain with the input string as the topic
    response = chain.invoke("hamster")
    # Return the response
    return  response
