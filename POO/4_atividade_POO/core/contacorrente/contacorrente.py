from core.saque.saque import Saque

class ContaCorrente():
    
    def __init__(self, saldo, banco, num_conta, num_agencia):
        self.__tipo_conta = "Conta Corrente"
        self.__saldo = saldo
        self.__num_conta = num_conta
        self.__num_agencia = num_agencia
        self.__banco = banco


    
    @property
    def saldo(self):
        return {
            "tipo_conta": self.__tipo_conta,
            "banco": self.__banco,
            "num_conta": self.__num_conta,
            "num_agencia": self.__num_agencia,
            "saldo": self.__saldo
        }
    
    
    @saldo.setter
    def saldo(self, deposito):
        self.saldo += deposito

    def sacar_cc(self, vl_saque):
        if self.__saldo > vl_saque:
            saque_cc = Saque.sacar(vl_saque, self.__saldo)
            self.__saldo -= saque_cc
            print("SUCESSO: Saque realizado, o saldo disponivel é: R$ {self.__saldo:.2f}".replace(".", ","))
        
        else:
            print("O valor solicitado é menor do que o valor disponivel na conta, valor disponivel para saque R$ {self.__saldo:.2f}".replace(".", ","))



    
        

    