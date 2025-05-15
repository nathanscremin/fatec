matriz = []

fr = input('Digite a frase que será lida em espiral: ')
n = int(input('Digite o numero N da matriz: '))

for i in range(0,n*n):
    if i < len(fr):
        letra = fr[i]
        matriz.append(letra)
    else:
         matriz.append('_')

ins = 1
q = ''

if n >= 0:
    for value in range(0,n*n):
        if value == (n*ins-1):
            q = '\n'
            ins += 1
        else:
            q = ''
        print(matriz[value], '', end=q)