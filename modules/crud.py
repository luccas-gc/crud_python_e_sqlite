import sqlite3

class ErrorDB(Exception):
    def __init__(self, message):
        self.message = f"Erro ao interagir com Banco de Dados: {message}"
        super().__init__(self.message)

class User:
    def __init__(self, nome: str, profession: str):
        self.nome = nome
        self.profession = profession

class Table:
    def __init__(self, db="database.db"):
        self.db = db

    def create_table(self):
        try:
            with sqlite3.connect(self.db) as conexao:
                cursor = conexao.cursor()

                comando = '''CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome varchar(30) NOT NULL,
                profissao varchar(30) NOT NULL
                )'''

                cursor.execute(comando)
                conexao.commit()
        except sqlite3.Error as Error:
            raise ErrorDB(Error)

    #Create
    def add_user(self, user: User):
        try:
            with sqlite3.connect(self.db) as conexao:
                cursor = conexao.cursor()

                comando = "INSERT INTO funcionarios (nome, profissao) VALUES (?, ?)"
                values = (user.nome, user.profession)
                cursor.execute(comando, values)
                conexao.commit()

                if cursor.rowcount > 0:
                    print("\nUsuário cadastrado.")
                else:
                    print("\n Não foi possível cadastrar o usuário..")
        
        except sqlite3.Error as Error:
            raise ErrorDB(Error)

    #Read
    def read_user(self):
        try:
            with sqlite3.connect(self.db) as conexao:
                cursor = conexao.cursor()

                comando = "SELECT * FROM funcionarios"
                cursor.execute(comando)
                dados = cursor.fetchall()

                return dados    
        
        except sqlite3.Error as Error:
            raise ErrorDB(Error)
        
    #Update
    def update_user(self, idUser: int, nome=None, profession=None):
        try:
            with sqlite3.connect(self.db) as conexao:
                cursor = conexao.cursor()
                
                if nome and not profession:
                    comando = "UPDATE funcionarios SET nome = ? WHERE id = ?"
                    values = (nome, idUser)
                    cursor.execute(comando, values)
                    conexao.commit()
                    if cursor.rowcount > 0:
                        print("\nNome Atualizado.")
                    else:
                        print("\nNão foi possível atualizar o usuário..")
                    
                elif profession and not nome:
                    comando = "UPDATE funcionarios SET profissao = ? WHERE id = ?"
                    values = (profession, idUser)
                    cursor.execute(comando, values)
                    conexao.commit()
                    if cursor.rowcount > 0:
                        print("\nProfissão Atualizado.")
                    else:
                        print("\nNão foi possível atualizar o usuário..")

                elif nome and profession:
                    comando = "UPDATE funcionarios SET nome = ?, profissao = ? WHERE id = ?"
                    values = (nome, profession, idUser)
                    cursor.execute(comando, values)
                    conexao.commit()
                    if cursor.rowcount > 0:
                        print("\nNome e Profissão Atualizado.")
                    else:
                        print("\nNão foi possível atualizar o usuário..")
                    
                else: 
                    print("\nOperação Cancelada.")

        except sqlite3.Error as Error:
            raise ErrorDB(Error)

    #Delete
    def delete_user(self, idUser: int):
        try:
            with sqlite3.connect(self.db) as conexao:
                cursor = conexao.cursor()

                comando = "DELETE FROM funcionarios WHERE id = ?"
                values = (idUser,)
                cursor.execute(comando, values)
                conexao.commit()

                if cursor.rowcount > 0:
                    print("\nUsuário Deletado.")
                else:
                    print("\nNão há Usuários com ese ID.")

        except sqlite3.Error as Error:
            raise ErrorDB(Error)

table = Table()

