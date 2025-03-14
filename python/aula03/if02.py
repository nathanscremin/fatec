min = int(input("Digite os minutos no mes: "))

if min < 200: 
    pr = 0.20
elif min < 400:
    pr = 0.18
else:
    pr = 0.15

print("Preço por minuto: " + str(pr))
total = min * pr
print("Total: " + str(total))