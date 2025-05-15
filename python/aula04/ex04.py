ida = int(input("Insira sua idade: "))

if ida < 14:
    print("Não pode entrar.")
    print("Não pode beber.")
elif ida < 18:
    print("Pode entrar com acompanhamento de responsáveis.")
    print("Não pode beber.")
elif ida >= 18:
    print("Pode entrar.")
    print("Pode beber.")