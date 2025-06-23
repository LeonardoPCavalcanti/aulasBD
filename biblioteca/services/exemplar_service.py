from db import SessionLocal
from models.exemplar import Exemplar

class ExemplarService:
    def __init__(self):
        self.session = SessionLocal()

    def criar(self, exemplar: Exemplar):
        self.session.add(exemplar)
        self.session.commit()

    def listar(self):
        return self.session.query(Exemplar).all()

    def buscar_por_id(self, tombo):
        return self.session.query(Exemplar).get(tombo)

    def atualizar(self, tombo, novos_dados: dict):
        exemplar = self.buscar_por_id(tombo)
        if exemplar:
            for chave, valor in novos_dados.items():
                setattr(exemplar, chave, valor)
            self.session.commit()

    def remover(self, tombo):
        exemplar = self.buscar_por_id(tombo)
        if exemplar:
            self.session.delete(exemplar)
            self.session.commit()
