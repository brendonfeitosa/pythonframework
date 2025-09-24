class Cliente:
    def __init__(self, nome, email, idade, data_nasc, genero):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.data_nasc = data_nasc
        self.genero = genero

    def exibir_informacoes(self):
        return self.nome, self.email, self.idade, self.data_nasc, self.genero