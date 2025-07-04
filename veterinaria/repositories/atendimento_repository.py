from sqlalchemy.orm import Session
from models.atendimento import Atendimento
from models.schemas import AtendimentoCreate

def criar_atendimento(db: Session, at: AtendimentoCreate):
    novo = Atendimento(**at.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_atendimentos(db: Session):
    return db.query(Atendimento).all()

def listar_por_pet(db: Session, pet_id: int):
    return db.query(Atendimento).filter(Atendimento.pet_id == pet_id).all()

def listar_por_veterinario(db: Session, vet_id: int):
    return db.query(Atendimento).filter(Atendimento.veterinario_id == vet_id).all()
