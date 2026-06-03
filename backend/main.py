from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from google import genai

from dotenv import load_dotenv
import os

# Cargar variables .env
load_dotenv()

# Obtener API KEY
api_key = os.getenv("GEMINI_API_KEY")

# Cliente Gemini
client = genai.Client(api_key=api_key)

# Crear app
app = FastAPI()

# Permitir conexión Reflex
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "Backend Gemini funcionando"}

# Modelo de datos
class Pregunta(BaseModel):
    pregunta: str

# Endpoint chat
@app.post("/chat")
async def chat(data: Pregunta):

    respuesta = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=data.pregunta
    )

    return {
        "respuesta": respuesta.text
    }