import json
import random
import time
from db import Database
from livro import Livro
from produtor1 import publish
from consts import *

def run():
    db = Database()
    db.create_tables()
    for _ in range(100):
        novoLivro = Livro( random.choice(NOMES_DE_LIVROS), random.choice(EDITORAS), random.choice(ANOS), random.randint(0, 4))
        inserted_id = db.insert_book(novoLivro)
        novoLivro.set_codigo(inserted_id)
        print("\nLivro cadastrado:", novoLivro)
        publish('criar_livro', json.dumps(novoLivro.to_dict()), str(novoLivro.genero))
        time.sleep(4)

run()