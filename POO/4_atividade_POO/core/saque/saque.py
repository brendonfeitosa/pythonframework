class Saque:
    """
    Utilitário simples para operações de saque.
    """
    def __init__(self, saque: float, saldo: float):
        self.__vl_saque = float(saque)
        self.__saldo = float(saldo)

    @property
    def valor(self) -> float:
        return self.__vl_saque

    def executar(self) -> float:
        """
        Tenta realizar o saque e retorna o novo saldo.
        Lança ValueError se não houver saldo suficiente.
        """
        if self.__vl_saque <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if self.__vl_saque > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        return self.__saldo - self.__vl_saque
