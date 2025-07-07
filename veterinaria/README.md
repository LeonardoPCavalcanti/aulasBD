
# 🐾 Sistema de Gerenciamento de Clínicas Veterinárias - FastAPI + PostgreSQL

Este projeto é uma API RESTful para o gerenciamento de uma rede de clínicas veterinárias, desenvolvido como atividade da disciplina de Banco de Dados. Utiliza **FastAPI**, **SQLAlchemy**, **PostgreSQL** e **Pydantic** com estrutura de camadas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn (servidor ASGI)
- Pydantic
- psycopg2 (driver PostgreSQL)

---

## 🗂️ Estrutura do Projeto

```
veterinaria/
├── api/                 # Rotas FastAPI (endpoints)
├── models/              # Modelos ORM (SQLAlchemy)
├── repositories/        # Operações de acesso ao banco
├── services/            # Lógica de negócio
├── database.py          # Conexão e sessão com o banco
├── main.py              # Inicialização da aplicação FastAPI
├── schemas.py           # Pydantic schemas
├── create_tables.py     # Script para criar tabelas no banco
├── popular_banco.py     # Script para popular o banco com dados de exemplo
└── requirements.txt     # Dependências do projeto
```

---

## ⚙️ Configuração da Conexão (`database.py`)

```python
DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/veterinaria_db"
```

- Substitua `1234` pela sua senha real
- Garanta que o banco `veterinaria_db` já existe

---

## 📦 Como rodar o projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/LeonardoPCavalcanti/aulasBD.git
cd veterinaria
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Crie as tabelas no banco

```bash
python create_tables.py
```

### 5️⃣ Popule o banco com dados de exemplo

```bash
python popular_banco.py
```

### 6️⃣ Inicie a API

```bash
uvicorn main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Endpoints principais

- `POST /clinicas`, `GET /clinicas`, `GET /clinicas/{id}`, `GET /clinicas/{id}/veterinarios`
- `POST /veterinarios`, `GET /veterinarios`, `GET /veterinarios/{id}/atendimentos`
- `POST /tutores`, `GET /tutores/{id}/pets`
- `POST /pets`, `GET /pets`, `GET /pets/{id}/atendimentos`
- `POST /atendimentos`, `GET /atendimentos`

---

## 📊 Scripts úteis

- `create_tables.py` → cria todas as tabelas no banco
- `popular_banco.py` → insere dados de exemplo (2 clínicas, 2 tutores, 2 pets, 2 atendimentos)

---

## 📑 Licença

Este projeto é acadêmico e pode ser usado livremente para fins didáticos.

---

## Desenvolvido por:
- Leonardo Pessoa Cavalcanti
- Lucas Marques dos Santos
- Erick Vinicius Justino da Silva

Disciplina de Banco de Dados – UFRN 
