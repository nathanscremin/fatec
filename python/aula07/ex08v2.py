while True:
    senha = input('Insira uma senha no verificador: ')

    len_senha = len(senha)
    echars = '!@#$%&*çÇ'
    upperchar = 'QWERTYIOPASDFGHJKLZXCVBNM'
    lowchar = upperchar.lower()
    num = '1234567890'

    hspc = any(char in echars for char in senha)
    upp = any(char in upperchar for char in senha)
    lww = any(char in lowchar for char in senha)
    nms = any(char in num for char in senha)

    condition = ''
    if senha != '':
        if len_senha < 8:
            condition += 'A senha atual tem menos de 8 carácteres / '
        if hspc == False:
            condition += 'Faltam carácteres especiais na senha / '
        if upp == False:
            condition += 'Faltam letras maiúsculas na senha / '
        if lww == False:
            condition += 'Faltam letras minúsculas na senha / '
        if nms == False:
            condition += 'Faltam números na senha / '
    else:
        print('Senha indefinida.')

    if condition != '':
        print('/ ' + condition)
    else:
        print('A senha é forte.')