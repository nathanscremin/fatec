id = int(input("Digite sua idade: "))
sl = int(input("Digite seu salário: "))

if id >= 60:
    print("Voce tem direito ao beneficio.")
elif id >= 18 and sl <= 2000:
    print("Voce tem direito ao beneficio.")
else:
    print("Voce não tem direito ao beneficio.")