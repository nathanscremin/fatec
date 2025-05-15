frase = input("Digite uma frase de Bom dia e Obrigado.:")
text = frase
frase = frase.lower()
if frase.startswith("bom dia"):
    print("A frase começa com bom dia.")
else:
    print("A frase não começa com bom dia.")
if frase.endswith("obrigado"):
    print("A frase acaba com obrigado.")
else:
    print("A frase não acaba com obrigado")
print(F"A frase é: {text}")