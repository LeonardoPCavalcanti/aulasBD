from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.schemas import TutorCreate, TutorRead
import services.tutor_service as tutor_service
import services.pet_service as pet_service

router = APIRouter(prefix="/tutores", tags=["Tutores"])

@router.post("/", response_model=TutorRead)
def criar_tutor(tutor: TutorCreate, db: Session = Depends(get_db)):
    return tutor_service.criar_tutor(db, tutor)

@router.get("/{id}/pets")
def listar_pets_do_tutor(id: int, db: Session = Depends(get_db)):
    return pet_service.listar_por_tutor(db, id)
