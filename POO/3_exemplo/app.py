from core.pessoa.pessoa import Pessoa

obj = Pessoa()

print(obj.nome)

obj.nome = "Gabriel"
obj.idade = 15

print(obj.nome)
print(obj.idade)

obj.nome = "Brendon"
obj.idade = 29

print(obj.nome)
print(obj.idade)

print("------------------------------")


print(obj.get_dados())

obj.set_dados("Anderson", 44)

print(obj.get_dados())



