numeros = [1, 3, 5, 7, 9]

print('Primeira forma:')
numeros2 = sorted(numeros, reverse=True)
men = 0
mai = 0
for n in numeros[0:4]:
    men += n
for n in numeros2[0:4]:
    mai += n
print(men,mai)

print("Segunda forma:")
print((sum(numeros) - max(numeros)), (sum(numeros) - min(numeros)))