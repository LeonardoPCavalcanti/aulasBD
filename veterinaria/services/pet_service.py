from sqlalchemy.orm import Session
from repositories import pet_repository
from models.schemas import PetCreate

def criar_pet(db: Session, pet: PetCreate):
    return pet_repository.criar_pet(db, pet)

def listar_pets(db: Session):
    return pet_repository.listar_pets(db)

def buscar_pet_por_id(db: Session, id: int):
    return pet_repository.buscar_por_id(db, id)

def listar_por_tutor(db: Session, tutor_id: int):
    return pet_repository.listar_por_tutor(db, tutor_id)
