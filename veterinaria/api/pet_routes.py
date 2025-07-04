from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.schemas import PetCreate, PetRead
import services.pet_service as pet_service
import services.atendimento_service as atendimento_service

router = APIRouter(prefix="/pets", tags=["Pets"])

@router.post("/", response_model=PetRead)
def criar_pet(pet: PetCreate, db: Session = Depends(get_db)):
    return pet_service.criar_pet(db, pet)

@router.get("/", response_model=list[PetRead])
def listar_pets(db: Session = Depends(get_db)):
    return pet_service.listar_pets(db)

@router.get("/{id}/atendimentos")
def listar_atendimentos_do_pet(id: int, db: Session = Depends(get_db)):
    return atendimento_service.listar_por_pet(db, id)
