frase = input("Insira uma frase:")
var = input("Insira a palavra que deseja procurar:")
if frase.count(var) >= 1:
    print(f"A palavra existe na frase, ela foi encontrada na posição {frase.find(var) + 1} na frase.")
else:
    print("A palavra não existe na frase.")