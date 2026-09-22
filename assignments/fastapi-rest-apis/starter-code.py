# Código inicial para a assignment de FastAPI
# Implemente a solução para a API REST abaixo.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Item(BaseModel):
    title: str
    description: str = ""
    price: float


items = [
    {"id": 1, "title": "Python Crash Course", "description": "A practical introduction to Python", "price": 29.99},
    {"id": 2, "title": "Fluent Python", "description": "Clear, readable, and idiomatic Python", "price": 45.50},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


# TODO: criar rota GET /items
# TODO: criar rota POST /items
# TODO: criar rota GET /items/{item_id}
# TODO: criar rota PUT /items/{item_id}
# TODO: criar rota DELETE /items/{item_id}
