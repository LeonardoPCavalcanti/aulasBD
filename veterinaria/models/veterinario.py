from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"))

    clinica = relationship("Clinica", back_populates="veterinarios")
    atendimentos = relationship("Atendimento", back_populates="veterinario")
