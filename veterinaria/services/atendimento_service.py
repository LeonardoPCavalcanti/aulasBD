from sqlalchemy.orm import Session
from repositories import atendimento_repository
from models.schemas import AtendimentoCreate

def criar_atendimento(db: Session, at: AtendimentoCreate):
    return atendimento_repository.criar_atendimento(db, at)

def listar_atendimentos(db: Session):
    return atendimento_repository.listar_atendimentos(db)

def listar_por_pet(db: Session, pet_id: int):
    return atendimento_repository.listar_por_pet(db, pet_id)

def listar_por_veterinario(db: Session, vet_id: int):
    return atendimento_repository.listar_por_veterinario(db, vet_id)
