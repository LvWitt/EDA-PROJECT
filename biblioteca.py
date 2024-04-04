from db import Database
from livro import Livro
from produtor import publish, publish2, publish_emprestimo
from tipos_livros import TIPOS_DE_LIVROS
import json

class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar(self, db):
        #codigo = int(input("\nDigite o Código: "))
        nome = input("Digite o Nome: ")
        editora = input("Digite a Editora: ")
        ano = input("Digite o Ano: ")
        tipos_disponiveis = ", ".join(TIPOS_DE_LIVROS)
        tipo = input("Digite o tipo do livro em numero (Tipos disponíveis: {}): ".format(tipos_disponiveis))

        novoLivro = Livro( nome, editora, ano,tipo)
        inserted_id = db.insert_book(novoLivro)
        novoLivro.set_codigo(inserted_id)
        publish('criar_livro', json.dumps(novoLivro.to_dict()), novoLivro.tipo)

    def consultar(self):
        #return self.livros
        buscar = input("\nBusca (digite 'todos' para listar todos os livros): ")
        publish2('buscar_livro', json.dumps(buscar))
        #chamar consumidor para esperar o retorno do publish
        #fazer print
    
    def emprestar(self):
        codigo_buscar = int(input("\nBusca por codigo do livro: "))
        db = Database()
        livro = db.fetch_available_book_by_id(codigo_buscar)
        #print(livro)
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