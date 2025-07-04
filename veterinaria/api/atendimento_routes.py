from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.schemas import AtendimentoCreate, AtendimentoRead
import services.atendimento_service as atendimento_service

router = APIRouter(prefix="/atendimentos", tags=["Atendimentos"])

@router.post("/", response_model=AtendimentoRead)
def criar_atendimento(atendimento: AtendimentoCreate, db: Session = Depends(get_db)):
    return atendimento_service.criar_atendimento(db, atendimento)

@router.get("/", response_model=list[AtendimentoRead])
def listar_atendimentos(db: Session = Depends(get_db)):
    return atendimento_service.listar_atendimentos(db)
