from fastapi import FastAPI, Depends
from sqlmodel import Session
from database import criardb, get_seccion
from models import Usuario
from crud import criar_usuario, listar_usuarios, buscar_usuario, atualizar_usuario, deletar_usuario
from chat import perguntar_gemini


app = FastAPI()

criardb()

@app.post("/usuarios/")
def criar(user: Usuario, session: Session = Depends(get_seccion())):
    return criar_usuario(session, user)

@app.get("/usuarios/")
def listar(session:  Session = Depends(get_seccion())):
    return listar_usuarios(session)

@app.get("/usuarios/{usuario_id}")
def buscar(usuario_id:  int, session: Session = Depends(get_seccion())):
    return buscar_usuario(session, usuario_id)

@app.put("/usuarios/{usuario_id}")
def atualiar(usuario_id: int, user: Usuario, session: Session = Depends(get_seccion())):
    return atualizar_usuario(session, usuario_id, user)

@app.delete("/usuarios/{usuario_id}")
def deletar(usuario_id = int, session: Session = Depends(get_seccion())):
    return deletar_usuario(session, usuario_id)


# CHAT
@app.post("/chat/")
async def chat(pergunta: str):
    return{"resposta": await perguntar_gemini(pergunta)}