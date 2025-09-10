def button_gravar_event():
    if check_var.get() == "on":
#Botão gravar
        nome = entry_nome.get()
        rua = entry_endereco.get()
        cep = entry_cep.get()
        cidade = entry_cidade.get()
        sexo = genero.get()
        idade = entry_idade.get()
        habilidades = textbox.get("0.0", "end").strip()
        checagem = check_var.get()

        conteudo = f""" 
        -------------------INFORMAÇÕES-------------------
        Nome: {nome}
        Endereço: {rua}
        CEP: {cep}
        Cidade: {cidade}
        Gênero: {sexo}
        Idade: {idade}
        Habilidades: {habilidades}
        Disponível para candidatura: {checagem}
        """
        arquivo = open("Curriculo.txt" , "w", encoding="utf-8")
        arquivo.write(conteudo)
        arquivo.close()

        msb.showinfo("Sucesso", "Dados gravados com sucesso no arquivo 'curriculo.txt'.")

        limpar_form = button_cancelar_event()

    else:
        print("Marque a caixa de seleção para seguir com o cadastro!")