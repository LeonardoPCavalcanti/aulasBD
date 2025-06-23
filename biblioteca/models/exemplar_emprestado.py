from sqlalchemy import Column, Integer, ForeignKey
from models import Base

class ExemplarEmprestado(Base):
    __tablename__ = "exemplar_emprestado"

    codigo_emprestimo = Column(Integer, ForeignKey("emprestimo.codigo"), primary_key=True)
    tombo_exemplar = Column(Integer, ForeignKey("exemplar.tombo"), primary_key=True)

    def __repr__(self):
        return f"<ExemplarEmprestado(codigo_emprestimo={self.codigo_emprestimo}, tombo_exemplar={self.tombo_exemplar})>"
