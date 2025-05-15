# enumerate
for i, letra in enumerate("python"):
    print(i, letra)

# zip
nm = ["Ana", "Bia", "Carlos"]
nt = [10, 9, 8]

for nm, nt in zip(nm,nt):
    print(f"{nm} tirou {nt}")

# list map
def quad(x):
    return x * x

num1 = [1, 2, 3]
resul = list(map(quad, num1))
print(resul) # [1, 4, 9]

# filter
def mq5(x):
    return x > 5

print(list(filter(mq5, [1, 6, 3, 7, 8, 10, 2])))

# any()
value = [True, False, True]
print(any(value)) # True
print(all(value)) # False

# range(start, stop, step)
for i in range(0,11,2):
    print(i)

# in e not in
if 'a' in 'banana':
    print("Tem")

if 'a' not in 'bnn':
    print("Não tem")

# .join()
letras2 = ['p', 'y', 't', 'h', 'o', 'n']
print(''.join(letras2))

# funes
frase = "Hello, world!"
print(frase.split())

# strip
texto2 = "  oi  "
print(texto2.strip())

# list compression
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

# lambda (função resumida)
quadrado = lambda x: x * x
print(quadrado(4))

def quadract(x): 
    return x * x
print(quadract(4))

# try
try:
    num3 = int(input("Digite um número: "))
except ValueError:
    print("Isso não é um número.")