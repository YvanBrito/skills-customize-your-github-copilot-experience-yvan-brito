# 📘 Atividade: FastAPI Authentication and Security

## 🎯 Objective

Build a secure FastAPI application that manages users and protected routes, practicing authentication, authorization basics, and safe API design.

## 📝 Tasks

### 🛠️ Create a user login API

#### Descrição
Create a simple authentication flow where users can register and log in to receive a token for protected endpoints.

#### Requisitos
O programa completo deve:

- Criar uma API com `FastAPI` e um modelo de usuário com `id`, `username` e `password`.
- Definir uma rota `POST /register` para registrar um novo usuário.
- Definir uma rota `POST /login` para validar as credenciais e retornar um token.
- Simular uma autenticação básica com um token em memória.
- Exemplo de payload:

```json
{
  "username": "alice",
  "password": "secret123"
}
```

- Exemplo de resposta de login:

```json
{
  "access_token": "demo-token",
  "token_type": "bearer"
}
```

### 🛠️ Protect routes with authentication

#### Descrição
Create endpoints that require a valid token before returning data.

#### Requisitos
O programa completo deve:

- Definir uma rota `GET /profile` acessível apenas com autenticação.
- Ler o token do cabeçalho `Authorization`.
- Retornar `401` quando o token estiver ausente ou inválido.
- Retornar o perfil do usuário autenticado quando o token for válido.
- Exemplo de resposta:

```json
{
  "username": "alice",
  "message": "Authenticated successfully"
}
```

### 🛠️ Add security best practices

#### Descrição
Improve the API so it handles invalid input and access control more safely.

#### Requisitos
O programa completo deve:

- Validar que `username` não esteja vazio.
- Validar que `password` tenha pelo menos 6 caracteres.
- Retornar `400` para entradas inválidas.
- Retornar `401` com uma mensagem clara para autenticação falha.
- Usar mensagens de erro em JSON, como:

```json
{
  "detail": "Invalid credentials"
}
```

- Explicar por que é importante nunca armazenar senhas em texto puro em aplicações reais.
