num = int(input("Digite sua idade: "))

if num < 0 or num > 140:
    print("Idade inválida.")
elif num >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")