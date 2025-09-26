from core.contacorrente.contacorrente import ContaCorrente
from core.contapoupanca.contapoupanca import ContaPoupanca

class Cliente(ContaCorrente, ContaPoupanca):
    def __init__(self, nome, data_nasc, cpf, endereco):
        ContaCorrente.__init__(self, )
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__cpf = cpf
        self.__endereco = endereco

    
    @property
    def dados_cliente(self):
        return {
            "nome": self.__nome,
            "data_nasc": self.__data_nasc,
            "cpf": self.__cpf,
            "endereco": self.__endereco
        }
    
    @dados_cliente.setter
    def dados_cliente(self, nome, data_nasc, cpf, endereco):
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__cpf = cpf
        self.__endereco = endereco
    


    
