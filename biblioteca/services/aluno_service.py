from db import SessionLocal
from models.aluno import Aluno

class AlunoService:
    def __init__(self):
        self.session = SessionLocal()

    def criar(self, aluno: Aluno):
        self.session.add(aluno)
        self.session.commit()

    def listar(self):
        return self.session.query(Aluno).all()

    def buscar_por_id(self, matricula):
        return self.session.query(Aluno).get(matricula)

    def atualizar(self, matricula, novos_dados: dict):
        aluno = self.buscar_por_id(matricula)
        if aluno:
            for chave, valor in novos_dados.items():
                setattr(aluno, chave, valor)
            self.session.commit()

    def remover(self, matricula):
        aluno = self.buscar_por_id(matricula)
        if aluno:
            self.session.delete(aluno)
            self.session.commit()
