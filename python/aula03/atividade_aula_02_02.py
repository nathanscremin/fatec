nt = int(input("Digite a nota do aluno: "))
if nt >= 90:
    print("Aprovado com Excelência.")
elif nt >= 70 and nt < 90:
    print("Aprovado.")
elif nt >= 50 and nt < 70:
    print("Em recuperação.")
else:
    print("Reprovado.")