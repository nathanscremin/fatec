num = input("Digite sua idade: ")

if num <= 12:
    print("Categoria: Infantil")
elif num <= 17:
    print("Categoria: Juvenil")
elif num <= 40:
    print("Categoria: Adulto")
else:
    print("Categoria: Veterano")