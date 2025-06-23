from db import SessionLocal
from models.emprestimo import Emprestimo

class EmprestimoService:
    def __init__(self):
        self.session = SessionLocal()

    def criar(self, emprestimo: Emprestimo):
        self.session.add(emprestimo)
        self.session.commit()

    def listar(self):
        return self.session.query(Emprestimo).all()

    def buscar_por_id(self, codigo):
        return self.session.query(Emprestimo).get(codigo)

    def atualizar(self, codigo, novos_dados: dict):
        emprestimo = self.buscar_por_id(codigo)
        if emprestimo:
            for chave, valor in novos_dados.items():
                setattr(emprestimo, chave, valor)
            self.session.commit()

    def remover(self, codigo):
        emprestimo = self.buscar_por_id(codigo)
        if emprestimo:
            self.session.delete(emprestimo)
            self.session.commit()
