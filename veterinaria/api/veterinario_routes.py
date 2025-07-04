from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.schemas import VeterinarioCreate, VeterinarioRead
import services.veterinario_service as vet_service

router = APIRouter(prefix="/veterinarios", tags=["Veterinários"])

@router.post("/", response_model=VeterinarioRead)
def criar_veterinario(vet: VeterinarioCreate, db: Session = Depends(get_db)):
    return vet_service.criar_veterinario(db, vet)

@router.get("/", response_model=list[VeterinarioRead])
def listar_veterinarios(db: Session = Depends(get_db)):
    return vet_service.listar_veterinarios(db)

@router.get("/{id}/atendimentos")
def listar_atendimentos_por_veterinario(id: int, db: Session = Depends(get_db)):
    return vet_service.buscar_veterinario_por_id(db, id).atendimentos
