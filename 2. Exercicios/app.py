import customtkinter as ctk
from tkinter import messagebox as msb

app = ctk.CTk()
app.title("Currículo")

# Definir tamanho da janela
largura = 600
altura = 600

# Pegar tamanho da tela
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

# Calcular posição x e y
pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2

# Aplicar geometria (tamanho + posição centralizada)
app.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

#nome
label_nome = ctk.CTkLabel(app, text="Nome completo", fg_color="transparent")
label_nome.grid(row=0, column=0, padx=10, pady=(10, 0), stick="w")
entry_nome = ctk.CTkEntry(app, placeholder_text="Digite seu nome aqui")
entry_nome.grid(row=1, column=0, columnspan=5, padx=0, pady=0, stick="ew")

#Endereço
label_endereco = ctk.CTkLabel(app, text="Endereço", fg_color="transparent")
label_endereco.grid(row=2, column=0, padx=10, pady=(10, 0), stick="w")
entry_endereco = ctk.CTkEntry(app, placeholder_text="Endereço")
entry_endereco.grid(row=3, column=0, columnspan=2, padx=0, pady=0, stick="w")

#CEP
label_cep = ctk.CTkLabel(app, text="CEP", fg_color="transparent")
label_cep.grid(row=2, column=3, padx=10, pady=(10, 0), stick="w")
entry_cep = ctk.CTkEntry(app, placeholder_text="CEP")
entry_cep.grid(row=3, column=3, padx=0, pady=0, stick="ew")

#Botão cep
def button_cep_event():
    print("button pressed")

button_cep = ctk.CTkButton(app, text="Buscar CEP", command=button_cep_event)
button_cep.grid(row=3, column=4, padx=10, pady=0, stick="w")

#Cidade
label_cidade = ctk.CTkLabel(app, text="Cidade", fg_color="transparent")
label_cidade.grid(row=4, column=0, padx=10, pady=(10, 0), stick="w")
entry_cidade = ctk.CTkEntry(app, placeholder_text="Cidade")
entry_cidade.grid(row=5, column=0, columnspan=5, padx=0, pady=0, stick="ew")

#Genero
label_genero = ctk.CTkLabel(app, text="Genero", fg_color="transparent")
label_genero.grid(row=6, column=0, padx=10, pady=(10, 0), stick="w")

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

genero = ctk.CTkOptionMenu(app, button_color="white",fg_color="white", values=["--------", "Masculino", "Feminino"], command=optionmenu_callback)
genero.set("--------")
genero.grid(row=7, column=0, columnspan=2, padx=0, pady=0, stick="w")

#Idade
label_idade = ctk.CTkLabel(app, text="Idade", fg_color="transparent")
label_idade.grid(row=6, column=3, padx=10, pady=(10, 0), stick="w")
entry_idade = ctk.CTkEntry(app, placeholder_text="Idade")
entry_idade.grid(row=7, column=3, columnspan=2, padx=0, pady=0, stick="w")

#Habilidades
label_habilidade = ctk.CTkLabel(app, text="Fale das suas habilidade", fg_color="transparent")
label_habilidade.grid(row=8, column=0, columnspan=5, padx=10, pady=(10, 0), stick="w")

textbox = ctk.CTkTextbox(app)
textbox.insert("0.0", "digite...")  # insert at line 0 character 0
text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
#textbox.delete("0.0", "end")  # delete all text
textbox.configure(state="disabled")  # configure textbox to be read-only
textbox.grid(row=9, column=0, columnspan=5, padx=0, pady=0, stick="ew")

#Autorização
def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

check_var = ctk.StringVar(value="off")
checkbox = ctk.CTkCheckBox(app, text="Disponibilizar meus dados para a candidatura", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
checkbox.grid(row=10, column=0, columnspan=4, padx=10, pady=(10, 0), stick="w")

#Botão cancelar
def button_cancelar_event():
    print("button pressed")

button_cancelar = ctk.CTkButton(app, text="Cancelar", command=button_cancelar_event)
button_cancelar.grid(row=11, column=0, padx=10, pady=(10, 0), stick="w")

#Botão gravar
def button_gravar_event():
    print("button pressed")

button_gravar = ctk.CTkButton(app, text="Gravar", command=button_gravar_event)
button_gravar.grid(row=11, column=3, padx=10, pady=(10, 0), stick="w")

app.mainloop()