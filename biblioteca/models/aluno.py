from sqlalchemy import Column, Integer, String
from models import Base

class Aluno(Base):
    __tablename__ = "aluno"

    matricula = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    curso = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Aluno(matricula={self.matricula}, nome='{self.nome}')>"
