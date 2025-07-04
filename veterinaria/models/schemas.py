from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# =========================
# Clinica
# =========================

class ClinicaBase(BaseModel):
    nome: str
    cidade: str

class ClinicaCreate(ClinicaBase):
    pass

class ClinicaRead(ClinicaBase):
    id: int

    class Config:
        orm_mode = True

class ClinicaWithVeterinarios(ClinicaRead):
    veterinarios: List["VeterinarioRead"] = []

# =========================
# Veterinario
# =========================

class VeterinarioBase(BaseModel):
    nome: str
    especialidade: str
    clinica_id: int

class VeterinarioCreate(VeterinarioBase):
    pass

class VeterinarioRead(VeterinarioBase):
    id: int

    class Config:
        orm_mode = True

class VeterinarioWithAtendimentos(VeterinarioRead):
    atendimentos: List["AtendimentoRead"] = []

# =========================
# Tutor
# =========================

class TutorBase(BaseModel):
    nome: str
    telefone: str

class TutorCreate(TutorBase):
    pass

class TutorRead(TutorBase):
    id: int

    class Config:
        orm_mode = True

class TutorWithPets(TutorRead):
    pets: List["PetRead"] = []

# =========================
# Pet
# =========================

class PetBase(BaseModel):
    nome: str
    especie: str
    idade: int
    tutor_id: int

class PetCreate(PetBase):
    pass

class PetRead(PetBase):
    id: int

    class Config:
        orm_mode = True

class PetWithAtendimentos(PetRead):
    atendimentos: List["AtendimentoRead"] = []

# =========================
# Atendimento
# =========================

class AtendimentoBase(BaseModel):
    data: Optional[datetime] = None
    descricao: str
    pet_id: int
    veterinario_id: int

class AtendimentoCreate(AtendimentoBase):
    pass

class AtendimentoRead(AtendimentoBase):
    id: int

    class Config:
        orm_mode = True

# =========================
# Resolver Referências Recursivas
# =========================

ClinicaWithVeterinarios.update_forward_refs()
VeterinarioWithAtendimentos.update_forward_refs()
TutorWithPets.update_forward_refs()
PetWithAtendimentos.update_forward_refs()
