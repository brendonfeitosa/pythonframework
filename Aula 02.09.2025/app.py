import customtkinter as ctk

app = ctk.CTk()
app.title("my app")

# Definir tamanho da janela
largura = 400
altura = 150

# Pegar tamanho da tela
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

# Calcular posição x e y
pos_x = (largura_tela - largura) // 2
pos_y = (altura_tela - altura) // 2

# Aplicar geometria (tamanho + posição centralizada)
app.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


def button_callback():
    print("button pressed")

def switch_event():
    status = switch_var.get()
    if status == "on":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")
   

ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

#customtkinter.set_appearance_mode("system")  # default
ctk.set_appearance_mode("light")
#customtkinter.set_appearance_mode("light")


switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(app, text="", command=switch_event, variable=switch_var, onvalue="on", offvalue="off")
switch.grid(row=0, column=0, padx=0, pady=0)

button = ctk.CTkButton(app, text="my button", command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20)

button_1 = ctk.CTkButton(app, text="my button", command=button_callback)
button_1.grid(row=1, column=1, padx=20, pady=20)

entry = ctk.CTkEntry(app, placeholder_text="CTkEntry")
entry.grid(row=2, column=0, columnspan=2, padx=20, pady=20, stick="ew")

app.mainloop()