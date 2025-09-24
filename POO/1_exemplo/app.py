from core.carro.carro import Carro

#instanciar a classe para construir o objeto
obj_honda_civic_xls = Carro(motor=140, modelo="xls")

obj_honda_civic_exs = Carro(motor=180, modelo="exs")

obj_honda_civic_lx = Carro(motor=100, modelo="lx")

#utilizar

cavalos = obj_honda_civic_exs.motor
modelo = obj_honda_civic_exs.modelo
rodas = obj_honda_civic_exs.rodas
print(f"Qtd Cavalos do modelo {modelo} : {cavalos} rodas {rodas}")

result = obj_honda_civic_exs.ligar_motor(False)
print(result)

result_2 = obj_honda_civic_exs.acelerar_carro()
print(result_2)

motor, modelo = obj_honda_civic_exs.get_informacoes()

print(f"INFO: motor ({motor}) modelo ({modelo})")