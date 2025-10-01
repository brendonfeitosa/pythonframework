from typing import Optional
from core.saque.saque import Saque

class ContaCorrente:
    def __init__(self, saldo: float, banco: str, num_conta: str, num_agencia: str, tipo_conta: str="Conta Corrente", limite: float=0.0):
        self.__saldo = float(saldo)
        self.__banco = str(banco)
        self.__num_conta = str(num_conta)
        self.__num_agencia = str(num_agencia)
        self.__tipo_conta = str(tipo_conta)
        self.__limite = float(limite)

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def banco(self) -> str:
        return self.__banco

    @property
    def num_conta(self) -> str:
        return self.__num_conta

    @property
    def num_agencia(self) -> str:
        return self.__num_agencia

    @property
    def tipo_conta(self) -> str:
        return self.__tipo_conta

    @property
    def limite(self) -> float:
        return self.__limite

    def depositar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O depósito deve ser positivo.")
        self.__saldo += float(valor)
        return self.__saldo

    def sacar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O saque deve ser positivo.")
        if valor > self.__saldo + self.__limite:
            raise ValueError("Saldo + limite insuficiente.")
        op = Saque(valor, self.__saldo)
        try:
            self.__saldo = op.executar()
        except ValueError:
            deficit = valor - self.__saldo
            if deficit <= self.__limite:
                self.__saldo = 0.0
                self.__limite -= deficit
            else:
                raise
        return self.__saldo

    def __repr__(self) -> str:
        return f"ContaCorrente (banco='{self.__banco}', agencia='{self.__num_agencia}', conta='{self.__num_conta}', saldo={self.__saldo:.2f}, limite={self.__limite:.2f})"
