from tkinter import *
from tkinter import ttk
root = Tk() #aqui cria um objeto através da classe Tk
frm = ttk.Frame(root, padding=10) #criou um objeto do tipo frame, e estou falando qu quero configurar ele dentro do root




frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text="Hello World!").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
ttk.Label(frm, text="Hello World!").grid(column=0, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)


root.mainloop()