import tkinter as tk
from tkinter import messagebox
import string

def verificar_senha():
    senha = entrada.get()
    erros = []

    if len(senha) < 8:
        erros.append("A senha tem menos de 8 caracteres.")
    if not any(c in '!@#$%&*çÇ' for c in senha):
        erros.append("Faltam caracteres especiais.")
    if not any(c.isupper() for c in senha):
        erros.append("Faltam letras maiúsculas.")
    if not any(c.islower() for c in senha):
        erros.append("Faltam letras minúsculas.")
    if not any(c.isdigit() for c in senha):
        erros.append("Faltam números.")

    if erros:
        resultado.config(text="\n".join(erros), fg="red")
    else:
        resultado.config(text="A senha é forte!", fg="green")

# Janela principal
janela = tk.Tk()
janela.title("Verificador de Senha")
janela.geometry("400x200")

# Widgets
tk.Label(janela, text="Digite sua senha:").pack(pady=5)
entrada = tk.Entry(janela, show="*", width=30)
entrada.pack(pady=5)

tk.Button(janela, text="Verificar", command=verificar_senha).pack(pady=10)
resultado = tk.Label(janela, text="", wraplength=350, justify="left")
resultado.pack(pady=10)

janela.mainloop()
