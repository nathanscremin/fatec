frase = input('Insira uma frase: ')
sakanade1 = frase[::-1]
print(f'A palavra de trás pra frente é {sakanade1}.')
sakanade2 = sakanade1.lower().replace(' ', '')
frase1 = frase.lower().replace(' ', '')
if sakanade2 == frase1:
    print('Ela é um palindromo.')
else:
    print('Ela não é um palindromo.')