import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("biblioteca.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS livro(codigo INTEGER PRIMARY KEY, nome TEXT, editora TEXT, ano INTEGER, situacao TEXT, genero TEXT)")

    def insert_book(self, livro):
        query = "INSERT INTO livro VALUES (NULL, ?, ?,?,?,?)"
        livro_data = (livro.nome, livro.editora, livro.ano, livro.situacao, livro.genero)
        self.cursor.execute(query, livro_data)
        self.conn.commit()
        return self.cursor.lastrowid

    def fetch_all_books(self):
        res = self.cursor.execute("SELECT * FROM livro")
        data = res.fetchall()
        return data

    def fetch_books_from_str(self, search_str):
        columns = ['nome', 'editora', 'ano', 'situacao']

        like_conditions = " OR ".join([f"{col} LIKE ?" for col in columns])
        params = ['%' + search_str + '%'] * len(columns)

        sql_query = f"SELECT * FROM livro WHERE ({like_conditions})"
        res = self.cursor.execute(sql_query, params)
        data = res.fetchall()
        return data

    def fetch_books_by_id(self, book_id):
        sql_query = "SELECT * FROM livro WHERE codigo = ?"
        res = self.cursor.execute(sql_query, (book_id,))
        data = res.fetchall()
        return data

    def fetch_available_book_by_id(self, book_id):
        sql_query = "SELECT * FROM livro WHERE codigo = ? AND situacao='disponível'"
        res = self.cursor.execute(sql_query, (book_id,))
        data = res.fetchall()
        return data

    def update_book_by_id(self, book_id):   
        sql_update_query = "UPDATE livro SET situacao = 'ocupado' WHERE codigo = ?"
        self.cursor.execute(sql_update_query, (book_id,))
        self.conn.commit()
        sql_query = "SELECT * FROM livro WHERE codigo = ?"
        res = self.cursor.execute(sql_query, (book_id,))
        data = res.fetchone()

        return data
