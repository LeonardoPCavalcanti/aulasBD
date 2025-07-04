from sqlalchemy.orm import Session
from models.veterinario import Veterinario
from models.schemas import VeterinarioCreate

def criar_veterinario(db: Session, vet: VeterinarioCreate):
    novo = Veterinario(**vet.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_veterinarios(db: Session):
    return db.query(Veterinario).all()

def buscar_por_id(db: Session, id: int):
    return db.query(Veterinario).filter(Veterinario.id == id).first()

def listar_por_clinica(db: Session, clinica_id: int):
    return db.query(Veterinario).filter(Veterinario.clinica_id == clinica_id).all()
