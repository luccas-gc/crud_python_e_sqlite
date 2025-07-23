# Projeto CRUD com SQLite3 - Python 🐍

Este projeto foi desenvolvido como uma forma de praticar conceitos fundamentais da programação com Python, incluindo:

- Programação Orientada a Objetos (POO)
- Manipulação de banco de dados com SQLite3
- Tratamento de erros com `try/except`
- Organização de código em múltiplas classes e arquivos
- Validação de entrada de Dados

---

## 📚 Sobre o Projeto

O sistema implementa um CRUD (Create, Read, Update, Delete) de usuários armazenados em um banco de dados SQLite. O programa possui um menu de opções que permite:

1. Adicionar usuários
2. Ver Registros
3. Atualizar usuário
4. Deletar usuário
5. Sair

As ações são executadas por meio de um menu de navegação no terminal.

---

## 🧠 Tecnologias e Conceitos Aplicados

- **Python**
- **SQLite3** como banco de dados local
- Classes como `User`, `Table` e exceções personalizadas com `ErrorDB`
- Blocos `try/except` para tratamento de erros
- Separação de responsabilidades entre arquivos Python
- Validação de dados inseridos para evitar nomes e profissões com números

---

## 🔎 Estrutura do Projeto

```
📦 crud sqlite
├── 📁 modules
├── ├── __init__.py
│   ├── crud.py
│   ├── options.py
│   └── verificadores.py
├── menu.py
└── README.md
```

---

Para testar o sistema basta clonar o repositório com `git clone (URL do repositório)`.
Ou simplesmente baixar os arquivos em "CODE > DOWNLOAD Zip".