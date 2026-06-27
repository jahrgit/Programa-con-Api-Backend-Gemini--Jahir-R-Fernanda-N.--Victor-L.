from fastapi import FastAPI
from pydantic import BaseModel

from backend.consultas_db import obtener_propietarios, obtener_datos_completos
from backend.gemini_service import responder_con_gemini

app = FastAPI()

class Pregunta(BaseModel):
    pregunta: str

@app.get("/")
def inicio():
    return {"mensaje": "Backend funcionando correctamente"}

@app.get("/propietarios")
def listar_propietarios():
    datos = obtener_propietarios()
    return {"propietarios": datos}

@app.post("/preguntar")
def preguntar(data: Pregunta):
    datos = obtener_datos_completos()
    respuesta = responder_con_gemini(data.pregunta, datos)

    return {
        "pregunta": data.pregunta,
        "respuesta": respuesta
    }