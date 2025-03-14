nome = input("Digite seu nome: ")
idade = str(int(input('Digite sua idade: '))) # Coloquei em int por costume, afinal estamos tratando de um numero.
altura = str(float(input('Digite sua altura (em metros, exemplo 1.80): '))) # Passei para float para ele resumir as casas, por exemplo 1.80 vira 1.8.
print("Meu nome é " + nome + ", tenho " + idade + " anos e tenho " + altura + " de altura.")