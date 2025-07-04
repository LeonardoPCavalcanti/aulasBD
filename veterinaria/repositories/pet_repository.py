from sqlalchemy.orm import Session
from models.pet import Pet
from models.schemas import PetCreate

def criar_pet(db: Session, pet: PetCreate):
    novo = Pet(**pet.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_pets(db: Session):
    return db.query(Pet).all()

def buscar_por_id(db: Session, id: int):
    return db.query(Pet).filter(Pet.id == id).first()

def listar_por_tutor(db: Session, tutor_id: int):
    return db.query(Pet).filter(Pet.tutor_id == tutor_id).all()
