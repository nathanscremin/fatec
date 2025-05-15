print("Código do Cargo")
print("Escriturário - 1")
print("Secretário - 2")
print("Caixa - 3")
print("Gerente - 4")
print("Diretor - 5")

cod = int(input("Insira o código do cargo: "))

if cod == 1:
    sal = 2500 + 300 - (2500 * (8/100))
elif cod == 2:
    sal = 3200 + 450 - (3200 * (10/100))
elif cod == 3:
    sal = 3800 + 600 - (3800 * (12/100))
elif cod == 4:
    sal = 7500 + 1000 - (7500 * (15/100))
elif cod == 5:
    sal = 12000 + 2000 - (12000 * (20/100))

print(f"Seu salário líquido é: {sal}")