a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Esses números formam um triâgulo equilátero.")
    elif a == b or a == c or b == c:
        print("Esses números formam um triâgulo isósceles.")
    else:
        print("Esses números formam um triâgulo escaleno.")
else:
    print("Esses números não formam um triângulo.")