class Cliente:
    def __init__(self, nome: str, data_nasc: str, cpf: str, endereco: str):
        # inicializa os atributos da instância
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.endereco = endereco

    def dados_cliente(self) -> str:
        """Retorna uma string com os dados do cliente."""
        return (f"Cliente: {self.nome}\n"
                f"Nascimento: {self.data_nasc}\n"
                f"CPF: {self.cpf}\n"
                f"Endereço: {self.endereco}")

    def __str__(self) -> str:
        # define como o objeto será mostrado ao usar print(obj)
        return self.dados_cliente()

