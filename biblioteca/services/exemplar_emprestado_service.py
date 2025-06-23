from db import SessionLocal
from models.exemplar_emprestado import ExemplarEmprestado

class ExemplarEmprestadoService:
    def __init__(self):
        self.session = SessionLocal()

    def criar(self, exemplar_emprestado: ExemplarEmprestado):
        self.session.add(exemplar_emprestado)
        self.session.commit()

    def listar(self):
        return self.session.query(ExemplarEmprestado).all()

    def buscar_por_id(self, codigo_emprestimo, tombo_exemplar):
        return self.session.query(ExemplarEmprestado).get((codigo_emprestimo, tombo_exemplar))

    def atualizar(self, codigo_emprestimo, tombo_exemplar, novos_dados: dict):
        item = self.buscar_por_id(codigo_emprestimo, tombo_exemplar)
        if item:
            for chave, valor in novos_dados.items():
                setattr(item, chave, valor)
            self.session.commit()

    def remover(self, codigo_emprestimo, tombo_exemplar):
        item = self.buscar_por_id(codigo_emprestimo, tombo_exemplar)
        if item:
            self.session.delete(item)
            self.session.commit()
