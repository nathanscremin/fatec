senha = input('Insira uma senha no verificador, ela deve conter caracteres especiais: ')
len_senha = len(senha)
print(len_senha)
fsenha = {
    0: senha.count('!'),
    1: senha.count('@'),
    2: senha.count('#'),
    3: senha.count('$'),
    4: senha.count('%'),
    5: senha.count('&'),
    6: senha.count('*')
}
counter = 0
for i, value in fsenha.items():
    if value > 0:
        counter += 1
    else: 
        if counter == 0:
            counter = 0
print(counter)
if len_senha > 8 and counter > 0:
    print('A senha é forte.')
elif len_senha > 8:
    print('Falta um character especial.')
elif counter > 0:
    print('Tem menos que 8 characters')
else:
    print('A senha tem menos de 8 characters e não tem character especial.')