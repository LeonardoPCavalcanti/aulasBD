from sqlalchemy import Column, Integer, Date, ForeignKey
from models import Base

class Emprestimo(Base):
    __tablename__ = "emprestimo"

    codigo = Column(Integer, primary_key=True)
    matricula_aluno = Column(Integer, ForeignKey("aluno.matricula"), nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date)
    data_devolucao_prevista = Column(Date, nullable=False)
    dias_atrasados = Column(Integer)

    def __repr__(self):
        return f"<Emprestimo(codigo={self.codigo}, matricula_aluno={self.matricula_aluno})>"
