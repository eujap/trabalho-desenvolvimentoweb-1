from fastapi import FastAPI, Depends, Body
from sqlmodel import Session
from database import criardb, get_session
from models import Usuario, Produto, Endereco
from crud import criar_usuario, listar_usuarios, buscar_usuario, atualizar_usuario, deletar_usuario,criar_produto,criar_endereco,listar_endereco, listar_produtos,atualizar_produto,atualizar_endereco,deletar_endereco,deletar_produto,buscar_endereco,buscar_produto
from chat import perguntar_gemini


app = FastAPI()

criardb()


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def home():
    return {"mensagem": "API FastAPI rodando! Use /docs para ver a documentação."}

@app.post("/usuarios/")
def criar(user: Usuario, session: Session = Depends(get_session)):
    return criar_usuario(session, user)

@app.get("/usuarios/")
def listar(session:  Session = Depends(get_session)):
    return listar_usuarios(session)

@app.get("/usuarios/{usuario_id}")
def buscar(usuario_id:  int, session: Session = Depends(get_session)):
    return buscar_usuario(session, usuario_id)

@app.put("/usuarios/{usuario_id}")
def atualiar(usuario_id: int, user: Usuario, session: Session = Depends(get_session)):
    return atualizar_usuario(session, usuario_id, user)

@app.delete("/usuarios/{usuario_id}")
def deletar(usuario_id = int, session: Session = Depends(get_session)):
    return deletar_usuario(session, usuario_id)

# PRODUTO
@app.post("/produtos/")
def criar(produto: Produto, session: Session = Depends(get_session)):
    return criar_produto(session, produto)

@app.get("/produtos/")
def listar(session:  Session = Depends(get_session)):
    return listar_produtos(session)

@app.get("/produtos/{produto_id}")
def buscar(produto_id:  int, session: Session = Depends(get_session)):
    return buscar_produto(session, produto_id)

@app.put("/produtos/{produto_id}")
def atualiar(produto_id: int, produto: Produto, session: Session = Depends(get_session)):
    return atualizar_produto(session, produto_id, produto)

@app.delete("/produtos/{produto_id}")
def deletar(produto_id = int, session: Session = Depends(get_session)):
    return deletar_produto(session, produto_id)

#ENDERECO
@app.post("/enderecos/")
def criar(endereco: Endereco, session: Session = Depends(get_session)):
    return criar_endereco(session, endereco)

@app.get("/enderecos/")
def listar(session: Session = Depends(get_session)):
    return listar_enderecos(session)

@app.get("/enderecos/{endereco_id}")
def buscar(endereco_id: int, session: Session = Depends(get_session)):
    return buscar_endereco(session, endereco_id)

@app.put("/enderecos/{endereco_id}")
def atualizar(endereco_id: int, endereco: Endereco, session: Session = Depends(get_session)):
    return atualizar_endereco(session, endereco_id, endereco)

@app.delete("/enderecos/{endereco_id}")
def deletar(endereco_id: int, session: Session = Depends(get_session)):
    return deletar_endereco(session, endereco_id)

# CHAT
@app.post("/chat/")
async def chat(pergunta: str = Body(...)):
    resposta = await perguntar_gemini(pergunta)
    return {"resposta": resposta}