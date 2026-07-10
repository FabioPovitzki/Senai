import tkinter as tk
from tkinter import messagebox, ttk
from fpdf import FPDF


def gerar_pdf():
    cliente = entrada_cliente.get()
    servico = combo_servico.get()
    valor = entrada_valor.get()

    if not cliente or not servico or not valor:
        messagebox.showwarning("ERRO", "Por favor, informe todos os campos")
        return

    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="ORDEM DE SERVIÇO", ln=1, align="C")
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"Cliente: {cliente}", ln=1)
        pdf.cell(200, 10, txt=f"Servico: {servico}", ln=1)
        pdf.cell(200, 10, txt=f"Valor: R$ {valor}", ln=1)

        pdf.output("ordem_de_servico.pdf")

        # Exibe mensagem de sucesso para o usuário
        messagebox.showinfo("Sucesso", "PDF gerado com sucesso!")

    except Exception as e:
        # Se ocorrer qualquer erro, exibe mensagem de erro
        messagebox.showerror("Erro", f"Erro ao gerar o PDF: {e}")


# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Gerador de Ordem de Serviço")
janela.geometry("380x220")

# Campo: CLIENTE
tk.Label(janela, text="Cliente:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
entrada_cliente = tk.Entry(janela, width=28)
entrada_cliente.grid(row=0, column=1, padx=10, pady=5)

# Campo: SERVIÇO
tk.Label(janela, text="Serviço:").grid(row=1, column=0, sticky="w", pady=5, padx=5)

servicos_disponiveis = [
    "Formatação de Computador",
    "Instalação do sistema Operacional",
    "Manutenção de rede",
    "Criação de site",
    "Suporte técnico",
]

combo_servico = ttk.Combobox(
    janela, values=servicos_disponiveis, width=26, state="readonly"
)
combo_servico.grid(row=1, column=1, padx=10, pady=5)

# Campo: VALOR (Adicionado, pois faltava na interface original)
tk.Label(janela, text="Valor:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
entrada_valor = tk.Entry(janela, width=28)
entrada_valor.grid(row=2, column=1, padx=10, pady=5)

# Botão para Gerar PDF (Adicionado para que a função possa ser executada)
botao_gerar = tk.Button(
    janela, text="Gerar PDF", command=gerar_pdf, bg="#4CAF50", fg="white"
)
botao_gerar.grid(row=3, column=0, columnspan=2, pady=15)

janela.mainloop()