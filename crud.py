from sqlmodel import Session, select
from models import Usuario

def criar_usuario(session: Session, usuario: Usuario):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

def listar_usuarios(session: Session):
    return session.exec(select(Usuario)).all()

def buscar_usuario(session: Session, usuario_id: int):
    return session.get(Usuario, usuario_id)

def atualizar_usuario(session: Session, usuario:  int, novos_dados: Usuario):
    usuario =  session.get(Usuario, usuario_id)
    if not usuario:
        return None
    usuario.nome = novos_dados.nome
    usuario.email = novos_dados.email
    usuario.idade = novos_dados.idade
    session.commit()
    session.refresh(usuario)
    return usuario

def deletar_usuario(session: Session, usuario_id: int):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        return None
    session.delete(usuario)
    session.commit()
    return usuario
