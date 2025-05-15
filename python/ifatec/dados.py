import tkinter as tk
from tkinter import ttk
import random

# Tema
tema_atual = "claro"

def aplicar_tema():
    if tema_atual == "claro":
        janela.configure(bg="white")
        for widget in janela.winfo_children():
            try:
                widget.configure(bg="white", fg="black")
            except:
                pass
        resultado_label.configure(bg="white", fg="black")
    else:
        janela.configure(bg="#2b2b2b")
        for widget in janela.winfo_children():
            try:
                widget.configure(bg="#2b2b2b", fg="white")
            except:
                pass
        resultado_label.configure(bg="#2b2b2b", fg="white")

def trocar_tema():
    global tema_atual
    tema_atual = "escuro" if tema_atual == "claro" else "claro"
    aplicar_tema()

def rolar_dado():
    try:
        tipo = int(var_dado.get().replace('d', ''))
        quantidade = int(entry_quantidade.get())
        modificador = int(entry_modificador.get())

        if quantidade <= 0:
            resultado_label.config(text="Quantidade deve ser maior que 0.", fg="red")
            return

        resultados = [random.randint(1, tipo) + modificador for _ in range(quantidade)]
        resultados.sort(reverse=True)
        texto_resultado = f"Rolagens (mod +{modificador}): {resultados}\nTotal: {sum(resultados)}"
        resultado_label.config(text=texto_resultado, fg="green")

    except ValueError:
        resultado_label.config(text="Entrada inválida.", fg="red")

# Janela
janela = tk.Tk()
janela.title("Rolador de Dados de RPG")
janela.geometry("430x300")
janela.resizable(False, False)

# Widgets
tk.Label(janela, text="Tipo de dado:").pack(pady=3)
var_dado = tk.StringVar(value="d20")
opcoes_dado = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
menu_dado = ttk.OptionMenu(janela, var_dado, *opcoes_dado)
menu_dado.pack()

tk.Label(janela, text="Quantidade de dados:").pack(pady=3)
entry_quantidade = tk.Entry(janela, width=5)
entry_quantidade.insert(0, "1")
entry_quantidade.pack()

tk.Label(janela, text="Modificador por dado:").pack(pady=3)
entry_modificador = tk.Entry(janela, width=5)
entry_modificador.insert(0, "0")
entry_modificador.pack()

tk.Button(janela, text="Rolar!", command=rolar_dado).pack(pady=10)
tk.Button(janela, text="Trocar tema (claro/escuro)", command=trocar_tema).pack()

resultado_label = tk.Label(janela, text="", wraplength=380, justify="center", font=("Courier", 12))
resultado_label.pack(pady=10)

aplicar_tema()
janela.mainloop()
