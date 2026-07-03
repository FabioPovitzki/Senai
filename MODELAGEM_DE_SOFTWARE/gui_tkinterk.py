import tkinter as tk
from tkinter import Tk

janela = tk.Tk()
janela.title("Financiamento de imóveis")
janela.geometry("400x200")

label = tk.Label(janela, text = "Insira sua matricula", font=("Arial",20))
label.pack(pady=20, padx=20)
texto = tk.Entry(janela,width=20)
texto.pack(pady=20)

janela.mainloop()


