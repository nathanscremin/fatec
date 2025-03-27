num = int(input("Digite sua idade: "))
gs = input("Você é gestante? (S/N): ")
df = input("Você é deficiente? (S/N): ")

if (df == "S" or df == "s") or num >= 60:
    print("Prioridade Máxima.")
elif gs == "S" or gs == "s":
    print("Prioridade Média.")
else:
    print("Atendimento Normal.")