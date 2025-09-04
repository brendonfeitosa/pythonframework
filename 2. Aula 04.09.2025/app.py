from core.calculo.media import calc_media, calc_media_pond #estou importando a função calc_media da pasta core/calculo/media.py

tupla_val = (10,5,7,6,3,4)
tupla_pesos = (1,1,3,1,3,1)
resultado = calc_media_pond(tupla_val, tupla_pesos)
print(f"Resultado da média ponderada {resultado}")


resultado_media = calc_media(*tupla_val)
print(f"Resultado da média {resultado_media}")