# Código inicial para a assignment de SQLite com FastAPI
# Implemente a API com persistência em banco de dados.

import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="SQLite Inventory API")


class Item(BaseModel):
    title: str
    description: str = ""
    price: float


def get_db_connection():
    conn = sqlite3.connect("items.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


@app.get("/")
def read_root():
    return {"message": "Welcome to the SQLite Inventory API"}


# TODO: criar rota GET /items
# TODO: criar rota POST /items
# TODO: criar rota GET /items/{item_id}
# TODO: criar rota PUT /items/{item_id}
# TODO: criar rota DELETE /items/{item_id}
