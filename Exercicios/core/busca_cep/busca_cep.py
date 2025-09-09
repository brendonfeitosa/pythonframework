import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            return dados
        else:
            return {"erro": "CEP não encontrado"}
    else:
        return {"erro": "Falha na requisição"}