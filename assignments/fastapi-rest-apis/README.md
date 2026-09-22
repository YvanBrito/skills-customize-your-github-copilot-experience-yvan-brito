# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API to manage a catalog of products or books, using FastAPI, request validation, and CRUD routes to practice API design and backend development.

## 📝 Tasks

### 🛠️ Create the FastAPI app

#### Descrição
Set up a FastAPI application and create an endpoint that returns a welcome message and confirms the API is running.

#### Requisitos
O programa completo deve:

- Instalar `fastapi` e `uvicorn`.
- Criar uma instância de `FastAPI()`.
- Definir uma rota `GET /` que retorne um JSON com uma mensagem de boas-vindas.
- Iniciar o servidor usando `uvicorn main:app --reload`.
- Exemplo de resposta:

```json
{
  "message": "Welcome to the Book API"
}
```

### 🛠️ Implement CRUD endpoints

#### Descrição
Crie endpoints para listar, criar, consultar, atualizar e remover itens de uma API em memória.

#### Requisitos
O programa completo deve:

- Definir um modelo `Item` com campos como `id`, `title`, `description` e `price`.
- Criar uma rota `GET /items` para listar todos os itens.
- Criar uma rota `POST /items` para adicionar um novo item.
- Criar uma rota `GET /items/{item_id}` para consultar um item específico.
- Criar uma rota `PUT /items/{item_id}` para atualizar um item.
- Criar uma rota `DELETE /items/{item_id}` para remover um item.
- Usar `pydantic` para validar os dados recebidos.
- Exemplo de payload:

```json
{
  "title": "Clean Code",
  "description": "A handbook of agile software craftsmanship",
  "price": 39.99
}
```

### 🛠️ Add validation and error handling

#### Descrição
Melhore a API adicionando validações, retorno de erros e comportamento mais robusto para entradas inválidas.

#### Requisitos
O programa completo deve:

- Garantir que `title` seja obrigatório e tenha pelo menos 1 caractere.
- Garantir que `price` seja maior ou igual a 0.
- Retornar `404` quando um item não for encontrado.
- Retornar `201` quando um item for criado com sucesso.
- Usar mensagens de erro claras e consistentes em JSON.
- Exemplo de resposta de erro:

```json
{
  "detail": "Item not found"
}
```
