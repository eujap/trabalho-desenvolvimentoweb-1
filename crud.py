from sqlmodel import Session, select
from models import Usuario, Produto, Endereco


def criar_usuario(session: Session, usuario: Usuario):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


def listar_usuarios(session: Session):
    return session.exec(select(Usuario)).all()


def buscar_usuario(session: Session, usuario_id: int):
    return session.get(Usuario, usuario_id)


def atualizar_usuario(session: Session, usuario_id: int, novos_dados: Usuario):
    usuario = session.get(Usuario, usuario_id)
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

def criar_produto(session: Session, produto: Produto):
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto

def listar_produtos(session: Session):
    return session.exec(select(Produto)).all()

def buscar_produto(session: Session, produto_id = int):
    return session.get(Produto, produto_id)

def atualizar_produto(session: Session, produto_id: int, novos_dados: Produto):
    produto = session.get(Produto, produto_id)
    if not produto:
        return None
    produto.nome = novos_dados.nome
    produto.preco = novos_dados.preco
    produto.estoque = novos_dados.estoque
    session.commit()
    session.refresh(produto)
    return produto

def deletar_produto(session: Session, produto_id: int):
    produto = session.get(Produto, produto_id)
    if not produto:
        return None
    session.delete(produto)
    session.commit()
    return produto


def criar_endereco(session: Session, endereco: Endereco):
    session.add(endereco)
    session.commit()
    session.refresh(endereco)
    return endereco


def listar_endereco(session: Session):
    return session.exec(select(Endereco)).all()


def buscar_endereco(session: Session, endereco_id=int):
    return session.get(Produto, endereco_id)


def atualizar_endereco(session: Session, endereco_id: int, novos_dados: Endereco):
    endereco = session.get(Endereco, endereco_id)
    if not endereco:
        return None
    endereco.rua = novos_dados.rua
    endereco.cidade = novos_dados.cidade
    endereco.estado = novos_dados.estado
    endereco.cep = novos_dados.cep
    session.commit()
    session.refresh(endereco)
    return endereco


def deletar_endereco(session: Session, endereco_id: int):
    endereco = session.get(Endereco, endereco_id)
    if not endereco:
        return None
    session.delete(endereco)
    session.commit()
    return endereco