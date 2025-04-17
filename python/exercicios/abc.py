abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abc2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ponto = '.'
alfa = ''
z = 0
tamanho = input('M ou m? ')
valor = int(input('Digite a quantidade de caracteres: '))-1

for x in abc:
    if tamanho == 'M':
        if z <= valor:
            alfa += abc2[z]
            z += 1
            print((ponto * (26 - z)) + alfa)
        else:
            break
    else:
        if z <= valor:
            alfa += abc[z]
            z += 1
            print((ponto * (26 - z)) + alfa)
        else:
            break