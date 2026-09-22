# Código inicial para a assignment de autenticação com FastAPI
# Implemente a lógica de registro, login e rotas protegidas.

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(title="Authentication API")


class UserCreate(BaseModel):
    username: str
    password: str


users_db = {}


@app.post("/register")
def register(user: UserCreate):
    # TODO: verificar se o usuário já existe
    # TODO: salvar usuário em users_db
    # TODO: retornar mensagem de sucesso
    pass


@app.post("/login")
def login(user: UserCreate):
    # TODO: validar credenciais
    # TODO: gerar token simples
    # TODO: retornar token
    pass


@app.get("/profile")
def profile(authorization: str = Header(default="")):
    # TODO: ler o cabeçalho Authorization
    # TODO: validar token
    # TODO: retornar dados do usuário autenticado
    pass
