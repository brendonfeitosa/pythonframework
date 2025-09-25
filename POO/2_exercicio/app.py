from core.cliente.cliente import Cliente
from core.produto.produto import Produto

# Produto
preco_prod1 = 5.50 # float(input("Digite o valor do produto 1: R$ "))
qtd_prod1 = 12 # int(input("Digite a quantidade do produto 1: "))
nome_prod1 = "coca-cola" # input("Digite o nome do produto 1: ")
prod_1 = Produto(nome_prod1, preco_prod1, qtd_prod1)

preco_prod2 = 2.5 # float(input("Digite o valor do produto 2: R$ "))
qtd_prod2 = 24 # int(input("Digite a quantidade do produto 2: "))
nome_prod2 = "tubaina" # input("Digite o nome do produto 2: ")
prod_2 = Produto(nome_prod2, preco_prod2, qtd_prod2)

preco_prod3 = 3.50 # float(input("Digite o valor do produto 3: R$ "))
qtd_prod3 = 12 # int(input("Digite a quantidade do produto 3: "))
nome_prod3 = "Skol" # input("Digite o nome do produto 3: ")
prod_3 = Produto(nome_prod3, preco_prod3, qtd_prod3)

# Exibindo informações dos produtos
print(f"Produto {prod_1.nome}, R$ {prod_1.preco:.2f}".replace(".", ","))
print(f"Produto {prod_2.nome}, R$ {prod_2.preco:.2f}".replace(".", ","))
print(f"Produto {prod_3.nome}, R$ {prod_3.preco:.2f}".replace(".", ","))

# Valor total dos produtos
vl_total_prod1 = prod_1.valor_total()
vl_total_prod2 = prod_2.valor_total()
vl_total_prod3 = prod_3.valor_total()

print(f"O valor total do produto {prod_1.nome} é: R$ {vl_total_prod1:.2f}".replace(".", ","))
print(f"O valor total do produto {prod_2.nome} é: R$ {vl_total_prod2:.2f}".replace(".", ","))
print(f"O valor total do produto {prod_3.nome} é: R$ {vl_total_prod3:.2f}".replace(".", ","))

# Cliente
nome_cliente_1 = "João" # input("Digite o nome do cliente: ")
email_cliente_1 = "joao@joao.com" # input("Digite o e-mail do cliente: ")
idade_cliente_1 = 26 # int(input("Digite a idade do cliente: "))
nascimento_cliente_1 = "19/01/1999" # input("Digite a data de nascimento: ")
genero_cliente_1 = "Masculino" # input("Digite o gênero: ")

cliente_1 = Cliente(nome_cliente_1, email_cliente_1, idade_cliente_1, nascimento_cliente_1, genero_cliente_1)

nome_cliente_2 = "Maria" # input("Digite o nome do cliente: ")
email_cliente_2 = "maria@maria.com" # input("Digite o e-mail do cliente: ")
idade_cliente_2 = 30 # int(input("Digite a idade do cliente: "))
nascimento_cliente_2 = "10/03/1993" # input("Digite a data de nascimento: ")
genero_cliente_2 = "Feminino" # input("Digite o gênero: ")

cliente_2 = Cliente(nome_cliente_2, email_cliente_2, idade_cliente_2, nascimento_cliente_2, genero_cliente_2)

nome_cliente_3 = "Carlos" # input("Digite o nome do cliente: ")
email_cliente_3 = "carlos@carlos.com" # input("Digite o e-mail do cliente: ")
idade_cliente_3 = 40 # int(input("Digite a idade do cliente: "))
nascimento_cliente_3 = "25/11/1983" # input("Digite a data de nascimento: ")
genero_cliente_3 = "Masculino" # input("Digite o gênero: ")

cliente_3 = Cliente(nome_cliente_3, email_cliente_3, idade_cliente_3, nascimento_cliente_3, genero_cliente_3)

# Exibindo os dados dos clientes
print(f"Dados do cliente 1: {cliente_1.exibir_informacoes()}")
print(f"Dados do cliente 2: {cliente_2.exibir_informacoes()}")
print(f"Dados do cliente 3: {cliente_3.exibir_informacoes()}")

# Exibindo o nome do cliente 1
print(f"Nome do cliente 1: {cliente_1.nome}")

# Exibindo a idade do cliente 1
print(f"A idade do cliente 1 é: {cliente_1.idade} anos")

# Exibindo o nome do produto 1
print(f"Nome do produto 1: {prod_1.nome}")

# Exibindo o preço do produto 1
print(f"Preço do produto 1: R$ {prod_1.preco:.2f}".replace(".", ","))
