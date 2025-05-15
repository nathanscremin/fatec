frase = input("Insira uma frase: ")
frase1 = frase.lower()
di = {
    'A': frase1.count('a'),
    'E': frase1.count('e'),
    'I': frase1.count('i'),
    'O': frase1.count('o'),
    'U': frase1.count('u')
}

print('Quantidade de vezes que cada vogal aparece:')
print(di)