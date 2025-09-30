class ContaPoupanca:
    def __init__(self, saldo: float, banco: str, num_conta: str, num_agencia: str, tipo_conta: str="Conta Poupança", rendimento_mensal: float=0.0):
        self.__saldo = float(saldo)
        self.__banco = str(banco)
        self.__num_conta = str(num_conta)
        self.__num_agencia = str(num_agencia)
        self.__tipo_conta = str(tipo_conta)
        self.__rendimento_mensal = float(rendimento_mensal)  # percentual, ex.: 0.6 = 0,6%

    @property
    def saldo(self) -> float:
        return self.__saldo

    def depositar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O depósito deve ser positivo.")
        self.__saldo += float(valor)
        return self.__saldo

    def sacar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= float(valor)
        return self.__saldo

    def render(self) -> float:
        """Aplica o rendimento mensal sobre o saldo e retorna o novo saldo."""
        if self.__rendimento_mensal > 0:
            self.__saldo *= (1 + self.__rendimento_mensal/100.0)
        return self.__saldo

    def __repr__(self) -> str:
        return f"ContaPoupanca (banco='{self.__banco}', agencia='{self.__num_agencia}', conta='{self.__num_conta}', saldo={self.__saldo:.2f}, rendimento_mensal={self.__rendimento_mensal:.2f}%)"
