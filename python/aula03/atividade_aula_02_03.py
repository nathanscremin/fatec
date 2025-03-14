alt = float(input("Digite sua altura (em Metros): "))
peso = float(input("Digite seu peso (em Quilos): "))

imc = peso/(alt**2)

if imc < 18.5:
    print("Abaixo do Peso.")
elif imc >= 18.5 and imc < 25:
    print("Peso Normal.")
elif imc >= 25 and imc < 30:
    print("Sobrepeso.")
elif imc >= 30 and imc < 35:
    print("Obesidade Grau 1.")
elif imc >= 35 and imc < 40:
    print("Obesidade Grau 2.")
else:
    print("Obesidade Grau 3 (mórbida)")