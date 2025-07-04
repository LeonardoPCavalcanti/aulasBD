from sqlalchemy.orm import Session
from repositories import tutor_repository
from models.schemas import TutorCreate

def criar_tutor(db: Session, tutor: TutorCreate):
    return tutor_repository.criar_tutor(db, tutor)

def buscar_tutor_por_id(db: Session, id: int):
    return tutor_repository.buscar_por_id(db, id)
