for i in range(0,10):
    sx = input("Insira seu sexo (M/F): ")
    idd = int(input("Insira sua idade: "))
    if sx == "M" or sx == "m":
        m1 += 1
    elif sx == "F" or sx == "f":
        f1 += 1

print(f"A quantidade de Homens foi: {m1}")
print(f"A quantidade de Mulheres foi: {f1}")
