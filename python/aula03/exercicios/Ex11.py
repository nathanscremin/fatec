import random
num = random.randint(1, 20)
print("Tente adivinhar o número secreto entre 1 e 20.")

while True:
    tent = int(input("Digite seu palpite: "))
    if tent > num:
        print("Muito alto!")
    elif tent < num:
        print("Muito baixo!")
    else:
        print("Parabéns! Você acertou!")
        break