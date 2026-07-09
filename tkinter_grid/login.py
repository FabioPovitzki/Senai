import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# JANELA PRINCIPAL

janela_principal = tk.Tk()
janela_principal.title("Sistema de Login")
janela_principal.geometry("350x200")

# FUNÇÃO LOGIN
def login():
    usuario = edt_login.get()
    senha = edt_senha.get()

    if usuario == "Fabio" and senha == "123":
       # messagebox.showinfo("Sucesso" ,"Login realizado com sucesso!")
       nova_janela = tk.Toplevel()
       nova_janela.title("Menu Principal")
       nova_janela.geometry("350x200")
       lbl_boas_vindas = tk.Label(
           nova_janela,
           text=f"Bem Vindo , {usuario}!",
           font=("Arial",14,"bold")  
       )
                    

       lbl_boas_vindas.pack(pady=30)

    else:
        messagebox.showerror("ERROR","Acesso Negado!")

# LOGIN
lbl_login = tk.Label(janela_principal,text="Login:")
lbl_login.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

# Campo de entrada e texto
edt_login = tk.Entry(
    janela_principal,
    width=35,    
)
edt_login.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
    )

# =====================================
# CAMPO ENTRADA DE SENHA
lbl_senha = tk.Label(janela_principal,text="Senha:")
lbl_senha.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

# Campo de entrada e texto
edt_senha = tk.Entry(
    janela_principal,
    width=35,
    show="*"    
)
edt_senha.grid(
    row=1,
    column=1,
    padx=10,
    pady=10    
    )

# BOTÃO LOGIN
btn_login = tk.Button(
    janela_principal,
    text="Login",
    command=login
)

btn_login.grid(
    row=2,
    column=0,
    columnspan=2, # mesclar a liha 2 coluna 0 com a 1
)



janela_principal.mainloop()
