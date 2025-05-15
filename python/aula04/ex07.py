n = int(input("Digite um numero:"))
fat = 1

for i in range(1,n+1):
    n2 = int(input("Digite um numero:"))
    for i in range(1,n2+1):
        fat = i*fat
    print(f"A fatorial de {i} é {fat}")
    fat = 1
