from sqlalchemy.orm import Session
from repositories import veterinario_repository
from models.schemas import VeterinarioCreate

def criar_veterinario(db: Session, vet: VeterinarioCreate):
    return veterinario_repository.criar_veterinario(db, vet)

def listar_veterinarios(db: Session):
    return veterinario_repository.listar_veterinarios(db)

def buscar_por_clinica(db: Session, clinica_id: int):
    return veterinario_repository.listar_por_clinica(db, clinica_id)

def buscar_veterinario_por_id(db: Session, id: int):
    return veterinario_repository.buscar_por_id(db, id)
