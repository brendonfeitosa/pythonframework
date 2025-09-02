import customtkinter

def button_callback():
    print("button pressed")

customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


#customtkinter.set_appearance_mode("system")  # default
customtkinter.set_appearance_mode("dark")
#customtkinter.set_appearance_mode("light")

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=1, padx=20, pady=20)
label1 = customtkinter.CTkLabel(app, text="Hello Word")
label1.grid(row=0, column=0, padx=20, pady=20)

entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry")
entry.grid(row=1, column=0, columnspan=2, padx=20, pady=20, stick="ew")

app.mainloop()