from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from google import genai
import json

load_dotenv()  # carrega o .env

API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)

app = FastAPI()

# Habilita CORS para testar localmente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # teste local
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API de Classificação de Emails com Gemini"}

@app.post("/classify/")
async def classify_email(text: str = Form(...)):
    prompt = f"""
    Você é um classificador de emails.
    Analise o email abaixo e responda **apenas em JSON** com:
    {{
        "categoria": "Produtivo ou Improdutivo",
        "resposta": "Mensagem curta sugerida"
    }}
    
    Email:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:

        result = response.text.strip().replace('```json', '').replace('```', '').strip()
        print(result)
    except json.JSONDecodeError:
    
        print("Erro ao decodificar JSON")

    return {"email": text, "classificacao": result}
