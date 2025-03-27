num = int(input("Digite o valor do saque: "))

notas_cem = int(num / 100)
num %= 100

notas_cinquenta = int(num / 50)
num = num % 50

notas_vinte = int(num / 20)
num = num % 20

notas_dez = int(num / 10)
num %= 10

print("Notas de R$ 100: " + str(notas_cem))
print("Notas de R$ 50: " + str(notas_cinquenta))
print("Notas de R$ 20: " + str(notas_vinte))
print("Notas de R$ 10: " + str(notas_dez))