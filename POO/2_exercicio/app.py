from core.cliente.cliente import Cliente
from core.produto.produto import Produto

#produto
preco_prod1 = 5.50 #float(input("Digite o valor do produto 1: R$ "))
qtd_prod1 = 12 #int(input("Digite a quantidade do produto 1: "))
nome_prod1 = "coca-cola" #input("Digite o nome do produto 1: ")
prod_1 = Produto(nome_prod1, preco_prod1, qtd_prod1)

preco_prod2 = 2.5 #float(input("Digite o valor do produto 2: R$ "))
qtd_prod2 = 24 #int(input("Digite a quantidade do produto 2: "))
nome_prod2 = "tubaina" #input("Digite o nome do produto 2: ")
prod_2 = Produto(nome_prod2, preco_prod2, qtd_prod2)

preco_prod3 = 3.50 #float(input("Digite o valor do produto 3: R$ "))
qtd_prod3 = 12 #int(input("Digite a quantidade do produto 3: "))
nome_prod3 = "Skol" #input("Digite o nome do produto 3: ")
prod_3 = Produto(nome_prod3, preco_prod3, qtd_prod3)

print(f"Produto {prod1.nome}, R$ {}")

#cliente
nome_cliente_1 = input("Digite o nome do cliente: ")
email_cliente_1 = input("Digite o e-mail do cliente: ")
idade_cliente_1 = int(input("Digite o e-mail do cliente: "))
nascimento_cliente_1 = int(input("Digite a idade: "))
genero_cliente_1 = input("Digite o gênero: ")

cliente_1 = Cliente(nome_cliente_1, email_cliente_1, idade_cliente_1, nascimento_cliente_1, genero_cliente_1)

nome_cliente_2 = input("Digite o nome do cliente: ")
email_cliente_2 = input("Digite o e-mail do cliente: ")
idade_cliente_2 = int(input("Digite o e-mail do cliente: "))
nascimento_cliente_2 = int(input("Digite a idade: "))
genero_cliente_2 = input("Digite o gênero: ")

cliente_2 = Cliente(nome_cliente_2, email_cliente_2, idade_cliente_2, nascimento_cliente_2, genero_cliente_2)

nome_cliente_3 = input("Digite o nome do cliente: ")
email_cliente_3 = input("Digite o e-mail do cliente: ")
idade_cliente_3 = int(input("Digite o e-mail do cliente: "))
nascimento_cliente_3 = int(input("Digite a idade: "))
genero_cliente_3 = input("Digite o gênero: ")

cliente_3 = Cliente(nome_cliente_3, email_cliente_3, idade_cliente_3, nascimento_cliente_3, genero_cliente_3)