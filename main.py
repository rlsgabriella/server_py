from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Hello word!"}
