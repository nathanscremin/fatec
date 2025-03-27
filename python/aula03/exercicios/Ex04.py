num = int(input("Digite sua idade: "))

if num < 0 or num > 140:
    print("Idade inválida.")
elif num <= 12 or num >= 60:
    print("O preço do ingresso é R$15.00")
else:
    print("O preço do ingresso é R$30.00")