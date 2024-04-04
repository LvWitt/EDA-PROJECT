class Livro:
    def __init__(self, nome, editora, ano,tipo):
        #self.codigo = codigo
        self.nome = nome
        self.editora = editora
        self.ano = ano
        self.situacao = 'disponível'
        self.tipo = tipo

    def __str__(self):
        return f"{self.codigo} : {self.nome}, {self.editora}, {self.ano}, {self.situacao}"

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome, 
            'editora': self.editora,
            'ano': self.ano, 
            'situacao': self.situacao,
            'tipo':self.tipo
        }
    def set_codigo(self, codigo):
        self.codigo = codigo