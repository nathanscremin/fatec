num = float(input("Digite a nota do aluno: "))

if num >= 7:
    print("Aluno aprovado.")
elif 5 < num < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")