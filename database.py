from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./db.sqlite"
engine = create_engine(DATABASE_URL, echo=True)

def criardb():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session