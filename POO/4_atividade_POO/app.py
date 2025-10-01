from core.cliente.cliente import Cliente
from core.contacorrente.contacorrente import ContaCorrente
from core.contapoupanca.contapoupanca import ContaPoupanca
import locale

# Define o locale para Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


print("===== TESTES DO SISTEMA BANCÁRIO =====\n")

# Cliente
cliente1 = Cliente(
    nome="José",
    data_nasc="17/10/2008",
    cpf="123.456.789-10",
    endereco="Rua ABC, 123"
)

print(">> Dados do Cliente:")
print(cliente1)
print("-" * 50)

# Conta Corrente 
cc = ContaCorrente(
    saldo=1000,
    banco="Banco do Brasil",
    num_conta="12345-6",
    num_agencia="0001",
    limite=200
)

print(">> Conta Corrente criada:", cc)

print("Depósito de R$ 500,00...")
cc.depositar(500)
print(f"Saldo atual: {locale.currency(cc.saldo, grouping=True)}")

print("Saque de R$ 1.200,00...")
cc.sacar(1200)
print(f"Saldo atual: {locale.currency(cc.saldo, grouping=True)}")
print("-" * 50)

# Conta Poupança
cp = ContaPoupanca(
    saldo=500,
    banco="Caixa",
    num_conta="98765-4",
    num_agencia="0001",
    rendimento_mensal=0.6
)

print(">> Conta Poupança criada:", cp)

print("Depósito de R$ 200,00...")
cp.depositar(200)
print(f"Saldo atual: {locale.currency(cp.saldo, grouping=True)}")

print("Saque de R$ 100,00...")
cp.sacar(100)
print(f"Saldo atual: {locale.currency(cp.saldo, grouping=True)}")

print("Aplicando rendimento mensal...")
cp.render()
print(f"Saldo após rendimento: {locale.currency(cp.saldo, grouping=True)}")
print("-" * 50)

