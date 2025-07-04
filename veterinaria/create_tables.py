from models.base import Base
from database import engine

# Importa todos os modelos para que o SQLAlchemy registre as tabelas
import models.clinica
import models.veterinario
import models.tutor
import models.pet
import models.atendimento

def criar_tabelas():
    print("🛠️ Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas criadas com sucesso!")

if __name__ == "__main__":
    criar_tabelas()
