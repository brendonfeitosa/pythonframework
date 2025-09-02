import customtkinter

def button_callback():
    print("button pressed")

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