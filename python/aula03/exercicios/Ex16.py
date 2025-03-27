num = float(input("Digite o seu salário: "))

if num <= 1900:
    print("Isento de Imposto.")
elif num <= 2800:
    imposto = num - (num * (7.5 / 100))
    print("Imposto de 7.5%.")
    print(num)
elif num <= 3700:
    imposto = num - (num * (15 / 100))
    print("Imposto de 15%.")
    print(num)
elif num <= 4600:
    imposto = num - (num * (22.5 / 100))
    print("Imposto de 22.5%.")
    print(num)
else:
    imposto = num - (num * (27.5 / 100))
    print("Imposto de 27.5%.")
    print(num)