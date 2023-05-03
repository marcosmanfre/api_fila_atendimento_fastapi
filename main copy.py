from fastapi import FastAPI
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select



class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    posicao: int
    nome: str
    chegada: Optional[int] = None



sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_clientes():
    cliente_1 = Cliente(posicao="1", nome="Marcos")
    cliente_2 = Cliente(posicao="2",nome="Abul")
    cliente_3 = Cliente(posicao="3",nome="Marcos2")
    cliente_4 = Cliente(posicao="4",nome="Marcos3")


    with Session(engine) as session:
        session.add(cliente_1)
        session.add(cliente_2)
        session.add(cliente_3)
        session.add(cliente_4)
        session.commit()



app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def home():
    return {"message": "API fila de atendimento"}

@app.get("/fila")
def exibir_fila():
    with Session(engine) as session:
        clientes = session.exec(select(Cliente)).all()
        return clientes

@app.get("/fila/{id}")
def retornar_cliente(id: int):
    return {"cliente": [cliente for cliente in create_clientes if cliente.id==id]}

@app.post("/fila")
def adicionar_fila(cliente: Cliente):
    with Session(engine) as session:
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente
        

@app.patch("/fila/{id}")
def atualizar_fila(id: int, posicao: Cliente):
    ...

@app.delete("/fila/{id}")
def apagar_fila():
    ...

def main():
    create_db_and_tables()
    create_clientes()

if __name__ == "__main__":
    main()