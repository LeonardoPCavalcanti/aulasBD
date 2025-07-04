from sqlalchemy.orm import Session
from models.tutor import Tutor
from models.schemas import TutorCreate

def criar_tutor(db: Session, tutor: TutorCreate):
    novo = Tutor(**tutor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def buscar_por_id(db: Session, id: int):
    return db.query(Tutor).filter(Tutor.id == id).first()
