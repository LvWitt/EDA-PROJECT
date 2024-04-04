from db import Database
from livro import Livro
from produtor1 import publish, publish_search, publish_emprestimo
from consts import GENEROS_DE_LIVROS
import json

class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar(self, db):
        nome = input("Digite o Nome: ")
        editora = input("Digite a Editora: ")
        ano = input("Digite o Ano: ")
        generos_disponiveis = ", ".join(GENEROS_DE_LIVROS)
        genero = input("Digite o genero do livro em numero \n(Gêneros disponíveis: {}): ".format(generos_disponiveis))

        novoLivro = Livro( nome, editora, ano, genero)
        inserted_id = db.insert_book(novoLivro)
        novoLivro.set_codigo(inserted_id)
        publish('criar_livro', json.dumps(novoLivro.to_dict()), novoLivro.genero)

    def consultar(self):
        buscar = input("\nDigite Codigo/Nome (digite 'todos' para listar todos os livros)\n: ")
        publish_search('buscar_livro', json.dumps(buscar))
    
    def emprestar(self):
        codigo_buscar = int(input("\nBusca por codigo do livro: "))
        db = Database()
        livro = db.fetch_available_book_by_id(codigo_buscar)

        if len(livro)>0:
            print(f"Item {codigo_buscar} disponível para empréstimo.")
            continuar = input("\nDeseja continuar o empréstimo? (s/n) ")
            if continuar == 's':
                res = db.update_book_by_id(codigo_buscar)
                print(f"\nItem emprestado:\n{res}\n")
                publish_emprestimo('emprestimo', json.dumps(res), res[5])
            else:
                return
        else:
            print(f"\nItem {codigo_buscar}, não disponível para empréstimo.\n")
            return
       
base = Biblioteca()