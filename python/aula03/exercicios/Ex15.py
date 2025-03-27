num = int(input("Digite a sua idade: "))
car = input("Você tem cartão de estudante? (S/N): ")

if num <= 6 or num >= 65:
    print("O passe é grátis.")
elif car == "S" or car == "s":
    print("O passe tem a metade do preço.")
else: 
    print("O passe tem o preço total.")