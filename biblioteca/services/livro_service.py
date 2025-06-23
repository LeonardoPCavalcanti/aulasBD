from db import SessionLocal
from models.livro import Livro

class LivroService:
    def __init__(self):
        self.session = SessionLocal()

    def criar(self, livro: Livro):
        self.session.add(livro)
        self.session.commit()

    def listar(self):
        return self.session.query(Livro).all()

    def buscar_por_id(self, codigo):
        return self.session.query(Livro).get(codigo)

    def atualizar(self, codigo, novos_dados: dict):
        livro = self.buscar_por_id(codigo)
        if livro:
            for chave, valor in novos_dados.items():
                setattr(livro, chave, valor)
            self.session.commit()

    def remover(self, codigo):
        livro = self.buscar_por_id(codigo)
        if livro:
            self.session.delete(livro)
            self.session.commit()
