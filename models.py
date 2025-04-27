from sqlmodel import SQLModel, Field
from typing import Optional

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    idade: int

class Produto(SQLModel, table=True):
    id: Optional[int] =  Field(default=None, primary_key=True)
    nome:str
    preco: float
    estoque: int

class Endereco(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    Rua: str
    cidade: str
    estado: str
    cep: str