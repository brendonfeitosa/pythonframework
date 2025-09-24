class Produto:
    def __init__(self, nome, preco, qtde):
        self.nome = nome
        self.preco = preco
        self.qtde = qtde
    
    def valor_total(self):
        return self.preco * self.qtde