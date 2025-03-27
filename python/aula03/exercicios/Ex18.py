user = input("Digite o nome de usuário: ")
i = 0 

while i < 3:
    senha = input("Digite a senha do usuário: ")
    if senha != "123":
        print("Senha incorreta")
        i += 1
        if i == 3:
            print("Login bloqueado, tenta novamente mais tarde.")
            break
    else:
        print("Bem-Vindo " + user +"! Login bem sucedido!")
        break