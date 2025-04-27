# 🚀 Projeto FastAPI + Streamlit + Gemini

Este projeto é o Trabalho T1 da disciplina de Programação Web, onde desenvolvemos:

## ✨ Funcionalidades

- CRUD completo para:
  - Usuários
  - Produtos
  - Endereços
- Integração com Inteligência Artificial Gemini (Google AI Studio) via endpoint `/chat/`
- Interface Web amigável usando Streamlit
- Organização profissional (uso de `.env`, `.gitignore`, `requirements.txt`)

---

## 📦 Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- SQLModel (ORM)
- Uvicorn (servidor ASGI)
- Streamlit (interface web)
- httpx (requisições HTTP)
- python-dotenv (variáveis de ambiente)

---

## 🛠️ Como Rodar o Projeto Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

```
### 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Configure o arquivo .env
GEMINI_API_KEY=sua-chave-api-do-gemini-aqui

 - Você pode obter a chave gratuita em: https://aistudio.google.com

### 5. Inicie o Backend (FastAPI)

uvicorn main:app --reload+

 - API disponível em: http://127.0.0.1:8000
 - Documentação Swagger em: http://127.0.0.1:8000/docs

### 5. Inicie Frontend
Em outra aba do terminal:
streamlit run app.py
 - Interface Web disponível em: http://localhost:8501

🌐 Endpoints da API
CRUD Usuários
 - POST /usuarios/ — Criar usuário
 - GET /usuarios/ — Listar usuários
 - GET /usuarios/{usuario_id} — Buscar usuário por ID
 - PUT /usuarios/{usuario_id} — Atualizar usuário
 - DELETE /usuarios/{usuario_id} — Deletar usuário

CRUD Produtos
 - POST /produtos/ — Criar produto
 - GET /produtos/ — Listar produtos
 - GET /produtos/{produto_id} — Buscar produto por ID
 - PUT /produtos/{produto_id} — Atualizar produto
 - DELETE /produtos/{produto_id} — Deletar produto

CRUD Endereços
 - POST /enderecos/ — Criar endereço
 - GET /enderecos/ — Listar endereços
 - GET /enderecos/{endereco_id} — Buscar endereço por ID
 - PUT /enderecos/{endereco_id} — Atualizar endereço
 - DELETE /enderecos/{endereco_id} — Deletar endereço

Integração com Gemini AI
 - POST /chat/
 - Entrada: pergunta em texto
 - Resposta: resposta gerada pela IA Gemini