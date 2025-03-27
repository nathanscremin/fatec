num = int(input("Digite o ano: "))

if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
    print("O ano é bissexto.")
else: 
    print("O ano não é bissexto.")