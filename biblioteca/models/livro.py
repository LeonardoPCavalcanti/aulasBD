from sqlalchemy import Column, Integer, String
from models import Base

class Livro(Base):
    __tablename__ = "livro"

    codigo = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    autor = Column(String(100), nullable=False)
    editora = Column(String(100), nullable=False)
    ano_publicacao = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Livro(codigo={self.codigo}, titulo='{self.titulo}')>"
