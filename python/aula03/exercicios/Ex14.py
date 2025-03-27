num = int(input("Digite a nota do aluno: "))

if 9 <= num <= 10:
    print("Conceito: A")
elif 7 <= num < 9:
    print("Conceito: B")
elif 5 <= num < 7:
    print("Conceito: C")
elif 3 <= num < 5:
    print("Conceito: D")
else:
    print("Conceito: F")