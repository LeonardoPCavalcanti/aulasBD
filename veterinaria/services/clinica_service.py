from sqlalchemy.orm import Session
from repositories import clinica_repository
from models.schemas import ClinicaCreate

def criar_clinica(db: Session, clinica: ClinicaCreate):
    return clinica_repository.criar_clinica(db, clinica)

def listar_clinicas(db: Session):
    return clinica_repository.listar_clinicas(db)

def buscar_clinica_por_id(db: Session, id: int):
    return clinica_repository.buscar_por_id(db, id)
