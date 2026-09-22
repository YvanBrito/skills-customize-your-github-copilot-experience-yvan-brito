# 📘 Atividade: Database Integration with SQLite and FastAPI

## 🎯 Objective

Build a small API that stores and retrieves data from a SQLite database, learning how FastAPI connects to persistent storage and how to manage records safely.

## 📝 Tasks

### 🛠️ Create the database layer

#### Descrição
Set up a SQLite database and create a table for storing products or tasks used by your API.

#### Requisitos
O programa completo deve:

- Criar uma conexão com SQLite usando `sqlite3`.
- Definir uma tabela chamada `items` com coluna `id`, `title`, `description` e `price`.
- Garantir que a tabela seja criada ao iniciar a API.
- Usar um arquivo local como `items.db` para persistência.
- Exemplo de estrutura da tabela:

```sql
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);
```

### 🛠️ Implement CRUD with database queries

#### Descrição
Create endpoints that read and write records from the SQLite database using FastAPI.

#### Requisitos
O programa completo deve:

- Criar uma rota `GET /items` para listar todos os itens.
- Criar uma rota `POST /items` para inserir um novo item.
- Criar uma rota `GET /items/{item_id}` para consultar um item específico.
- Criar uma rota `PUT /items/{item_id}` para atualizar um item existente.
- Criar uma rota `DELETE /items/{item_id}` para remover um item.
- Usar `sqlite3.Row` ou dicionários para transformar os resultados em JSON.
- Exemplo de payload:

```json
{
  "title": "Clean Architecture",
  "description": "A handbook for better software structure",
  "price": 42.50
}
```

### 🛠️ Add validation and robust responses

#### Descrição
Improve the API so it handles invalid data and missing records gracefully.

#### Requisitos
O programa completo deve:

- Validar que `title` seja obrigatório.
- Validar que `price` seja maior ou igual a 0.
- Retornar `404` quando o item solicitado não existir.
- Retornar `201` quando um item for criado com sucesso.
- Tratar erros de banco de dados com respostas claras em JSON.
- Exemplo de erro:

```json
{
  "detail": "Item not found"
}
```
