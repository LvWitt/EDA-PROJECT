from consts import GENEROS_DE_LIVROS


class Livro:
    def __init__(self, nome, editora, ano, genero):
        self.nome = nome
        self.editora = editora
        self.ano = ano
        self.situacao = 'disponível'
        self.genero = genero

    def __str__(self):
        return f"{self.codigo} : {self.nome}, {self.editora}, {self.ano}, {self.situacao}, {GENEROS_DE_LIVROS[self.genero]}"

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome, 
            'editora': self.editora,
            'ano': self.ano, 
            'situacao': self.situacao,
            'genero':self.genero
        }
    def set_codigo(self, codigo):
        self.codigo = codigo