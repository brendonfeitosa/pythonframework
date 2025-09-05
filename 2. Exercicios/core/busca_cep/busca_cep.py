import requests

def busca_cep(cep_form):
    cep = cep_form.replace("-", "").strip()
    url = f"https://viacep.com.br/ws{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        if 'erro' not in dados:
            return dados
        else:
            return "CEP não encontrado, digite novamete!"
    else:
        return "Erro na solicitação!"