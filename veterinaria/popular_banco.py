from database import SessionLocal
from models.clinica import Clinica
from models.veterinario import Veterinario
from models.tutor import Tutor
from models.pet import Pet
from models.atendimento import Atendimento
from datetime import datetime

def popular():
    db = SessionLocal()

    # Clínicas
    clinica1 = Clinica(nome="Clínica São Francisco", cidade="Natal")
    clinica2 = Clinica(nome="Clínica Pet Vida", cidade="Parnamirim")
    db.add_all([clinica1, clinica2])
    db.commit()

    # Veterinários
    vet1 = Veterinario(nome="Dr. Carlos", especialidade="Dermatologia", clinica_id=clinica1.id)
    vet2 = Veterinario(nome="Dra. Larissa", especialidade="Cirurgia", clinica_id=clinica2.id)
    db.add_all([vet1, vet2])
    db.commit()

    # Tutores
    tutor1 = Tutor(nome="Mariana Lima", telefone="84999990001")
    tutor2 = Tutor(nome="Felipe Souza", telefone="84999990002")
    db.add_all([tutor1, tutor2])
    db.commit()

    # Pets
    pet1 = Pet(nome="Bolt", especie="Cachorro", idade=3, tutor_id=tutor1.id)
    pet2 = Pet(nome="Mimi", especie="Gato", idade=2, tutor_id=tutor2.id)
    db.add_all([pet1, pet2])
    db.commit()

    # Atendimentos
    at1 = Atendimento(data=datetime(2024, 7, 1, 10, 30), descricao="Consulta dermatológica", pet_id=pet1.id, veterinario_id=vet1.id)
    at2 = Atendimento(data=datetime(2024, 7, 2, 14, 0), descricao="Cirurgia de castração", pet_id=pet2.id, veterinario_id=vet2.id)
    db.add_all([at1, at2])
    db.commit()

    db.close()
    print("✅ Banco populado com sucesso!")

if __name__ == "__main__":
    popular()
