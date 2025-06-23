from db import SessionLocal
from sqlalchemy import text
from models.aluno import Aluno
from models.livro import Livro
from models.exemplar import Exemplar
from models.emprestimo import Emprestimo
from models.exemplar_emprestado import ExemplarEmprestado

from services.aluno_service import AlunoService
from services.livro_service import LivroService
from services.exemplar_service import ExemplarService
from services.emprestimo_service import EmprestimoService
from services.exemplar_emprestado_service import ExemplarEmprestadoService


def main():
    # Testando conexão
    session = SessionLocal()
    try:
        session.execute(text("SELECT 1"))
        print("Conectado com sucesso! 🎉")
    except Exception as e:
        print("Erro na conexão:", e)
    finally:
        session.close()

    # ==== TESTES COM ALUNO ====
    aluno_service = AlunoService()

    # Criar aluno
    novo_aluno = Aluno(matricula=9999, nome="Leonardo Cavalcanti", email="leonardo@gmail.com", curso="Computação")
    aluno_service.criar(novo_aluno)

    # Listar alunos
    print("📝 Lista de alunos:")
    for aluno in aluno_service.listar():
        print(aluno)

    # Buscar aluno específico
    print("🔍 Buscando aluno 9999")
    aluno = aluno_service.buscar_por_id(9999)
    print(aluno)

    # Atualizar aluno
    aluno_service.atualizar(9999, {"nome": "Leonardo Atualizado"})
    print("🔧 Aluno atualizado:", aluno_service.buscar_por_id(9999))

    # Remover aluno
    aluno_service.remover(9999)
    print("❌ Aluno removido:", aluno_service.buscar_por_id(9999))

    # ==== TESTES COM LIVRO ====
    livro_service = LivroService()
    print("\n📚 Lista de livros:")
    for livro in livro_service.listar():
        print(livro)

    # ==== TESTES COM EXEMPLAR ====
    exemplar_service = ExemplarService()
    print("\n📦 Lista de exemplares:")
    for exemplar in exemplar_service.listar():
        print(exemplar)

    # ==== TESTES COM EMPRESTIMO ====
    emprestimo_service = EmprestimoService()
    print("\n🔗 Lista de empréstimos:")
    for emp in emprestimo_service.listar():
        print(emp)

    # ==== TESTES COM EXEMPLAR_EMPRESTADO ====
    exemplar_emprestado_service = ExemplarEmprestadoService()
    print("\n📦 Lista de exemplares emprestados:")
    for ee in exemplar_emprestado_service.listar():
        print(ee)


if __name__ == "__main__":
    main()
