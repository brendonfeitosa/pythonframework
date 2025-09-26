class Saque:

    def __init__(self, saque, saldo):
        self.__vl_saque = saque
        self.__saldo = saldo

    

    def sacar(self, saque, saldo):
        self.vl_saque = saque
        self.__saldo = saldo

        novo_saldo = self.__saldo - self.__vl_saque

        return  novo_saldo


