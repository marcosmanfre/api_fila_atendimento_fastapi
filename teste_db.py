from datetime import datetime
from lib2to3.pytree import Base
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field, create_engine



class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    posicao: int
    nome: str
    chegada: int

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)




SQLModel.metadata.create_all(engine)



@app.get("/")
async def home():
    return {"message": "API fila de atendimento"}

'''@app.get("/fila")
def exibir_fila():
    return {"cliente": db_clientes}

@app.get("/fila/{id}")
def retornar_cliente(id: int):
    return {"cliente": [cliente for cliente in db_clientes if cliente.id==id]}

@app.post("/fila")
def adicionar_fila():
    ...

@app.patch("/fila/{id}")
def atualizar_fila(id: int, posicao: Cliente):
    ...

@app.delete("/fila/{id}")
def apagar_fila():
    ...'''