class ContaPoupanca:
    
    def __init__(self, saldo, banco, num_conta, num_agencia, tx_juros):
        self.__tipo_conta = "Conta Poupança"
        self.__saldo = saldo
        self.__num_conta = num_conta
        self.__num_agencia = num_agencia
        self.__banco = banco
        self.__juros = tx_juros


    
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