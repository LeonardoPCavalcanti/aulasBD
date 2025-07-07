
# 📚 Sistema de Gerenciamento de Biblioteca com ORM (PostgreSQL + SQLAlchemy)

Este projeto foi desenvolvido como atividade da disciplina de Banco de Dados, utilizando **PostgreSQL**, **SQLAlchemy (ORM)** e **Python**.

---

## 🚀 Tecnologias Utilizadas
- Python
- PostgreSQL
- SQLAlchemy (ORM)
- psycopg2 (Driver PostgreSQL)

---

## 🗂️ Estrutura do Projeto

```
biblioteca/
│
├── models/                       # Mapeamento ORM das tabelas
│   ├── aluno.py
│   ├── livro.py
│   ├── exemplar.py
│   ├── emprestimo.py
│   └── exemplar_emprestado.py
│
├── services/                     # Classes de serviço (CRUD)
│   ├── aluno_service.py
│   ├── livro_service.py
│   ├── exemplar_service.py
│   ├── emprestimo_service.py
│   └── exemplar_emprestado_service.py
│
├── db.py                          # Conexão com PostgreSQL
├── main.py                        # Script principal de testes
├── requirements.txt               # Dependências do projeto
└── .gitignore                     # Arquivos ignorados no GitHub
```

---

## 🔗 Configuração da Conexão com o Banco (db.py)

No arquivo `db.py`, configure sua string de conexão:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://usuario:senha@localhost:5432/biblioteca_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
```

🔑 Substitua:
- `usuario`: Seu usuário do PostgreSQL
- `senha`: Sua senha do PostgreSQL
- `localhost`: Endereço do servidor (se local, mantém `localhost`)
- `5432`: Porta padrão do PostgreSQL
- `biblioteca_db`: Nome do seu banco de dados

---

## 🐍 Como rodar o projeto

### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Crie um ambiente virtual:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4️⃣ Verifique a conexão com o banco de dados no arquivo `db.py`.

### 5️⃣ Execute o programa:
```bash
python main.py
```

---

## 🏗️ Observação Importante
- Este projeto **não cria as tabelas automaticamente**.  
Você precisa ter previamente criado o banco de dados e suas tabelas no PostgreSQL (via SQL ou pgAdmin).

---

## ✅ Funcionalidades
- CRUD completo para as entidades:
  - Aluno
  - Livro
  - Exemplar
  - Empréstimo
  - Exemplar Emprestado
- Leitura de dados
- Inserção
- Atualização
- Remoção

---

## 💡 Boas práticas aplicadas
- Uso de ambiente virtual (`venv`)
- Separação clara de responsabilidades:
  - Models → Mapas das tabelas
  - Services → Operações CRUD
- Uso de `.gitignore` para ignorar arquivos locais e sensíveis
- Documentação clara no `README.md`

---

## Desenvolvido por:
- Leonardo Pessoa Cavalcanti
- Lucas Marques dos Santos
- Erick Vinicius Justino da Silva

"""
