num = int(input("Digite o seu salário: "))

if num < 2000:
    bonus = num + (num * (20 / 100))
    print(f"Seu novo salário é: {bonus}")
elif num < 5000:
    bonus = num + (num * (10 / 100))
    print(f"Seu novo salário é: {bonus}")
else:
    bonus = num + (num * (5 / 100))
    print(f"Seu novo salário é: {bonus}")