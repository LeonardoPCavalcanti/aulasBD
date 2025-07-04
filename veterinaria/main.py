from fastapi import FastAPI
from api import (
    clinica_routes,
    veterinario_routes,
    tutor_routes,
    pet_routes,
    atendimento_routes
)

app = FastAPI(
    title="API de Clínicas Veterinárias 🐶🐱",
    version="1.0.0"
)

# Registro dos endpoints
app.include_router(clinica_routes.router)
app.include_router(veterinario_routes.router)
app.include_router(tutor_routes.router)
app.include_router(pet_routes.router)
app.include_router(atendimento_routes.router)

# Mensagem de verificação
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API de Clínicas Veterinárias 🐾"}
