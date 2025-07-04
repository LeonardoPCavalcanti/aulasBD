from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.schemas import ClinicaCreate, ClinicaRead, ClinicaWithVeterinarios
import services.clinica_service as clinica_service
import services.veterinario_service as veterinario_service

router = APIRouter(prefix="/clinicas", tags=["Clínicas"])

@router.post("/", response_model=ClinicaRead)
def criar_clinica(clinica: ClinicaCreate, db: Session = Depends(get_db)):
    return clinica_service.criar_clinica(db, clinica)

@router.get("/", response_model=list[ClinicaRead])
def listar_clinicas(db: Session = Depends(get_db)):
    return clinica_service.listar_clinicas(db)

@router.get("/{id}", response_model=ClinicaRead)
def buscar_clinica(id: int, db: Session = Depends(get_db)):
    clinica = clinica_service.buscar_clinica_por_id(db, id)
    if not clinica:
        raise HTTPException(status_code=404, detail="Clínica não encontrada")
    return clinica

@router.get("/{id}/veterinarios", response_model=list)
def listar_veterinarios_da_clinica(id: int, db: Session = Depends(get_db)):
    return veterinario_service.buscar_por_clinica(db, id)
