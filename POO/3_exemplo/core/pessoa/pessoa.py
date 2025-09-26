class Pessoa:

    def __init__(self):
        self.__nome = ""
        self.__idade = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    
    def get_dados(self):
        return {
            "nome" : self.__nome,
            "idade" : self.__idade
        }
    
    def set_dados(self, novo_nome, nova_idade):
        self.__nome = novo_nome
        self.__idade = nova_idade