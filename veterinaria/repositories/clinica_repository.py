from sqlalchemy.orm import Session
from models.clinica import Clinica
from models.schemas import ClinicaCreate

def criar_clinica(db: Session, clinica: ClinicaCreate):
    nova = Clinica(**clinica.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_clinicas(db: Session):
    return db.query(Clinica).all()

def buscar_por_id(db: Session, id: int):
    return db.query(Clinica).filter(Clinica.id == id).first()
