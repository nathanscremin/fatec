#União de Strings
name = 'Ana'
age = 27
message = f"Meu nome é {name}, tenho {age} anos."
print(message)

#Medir o tamanho da string
len(message)

#Pega quantos characteres eu quero
message[23]
message[0:3] #De 0 a 3
message[0]

#Começa com ou termina com
message.startswith('Meu')
message.endswith('anos.')

#Conta a quantidade de characteres
String = "Um tigre, dois tigres, três tigres."
String.count('tigre')
String.find('tigre')
String.find('tigre', 10)

#Ponto e virgula
money = 300.0000000000
Credit = f"Meu crédito é: ${money:.2f}"
print(Credit)

#Posição da String
Str2 = 'Fatec'
'X' + Str2.center(20, '.') + 'X'
Str2.ljust(20)
Str2.rjust(20)

#Quebrar string
Item = 'Brr Brr Patapim'
Item.split(' ')
List = Item.split(' ')
Item.replace('Patapim', 'Bombardino Crocodillo')

#Valição de conteúdo
s = '1234'
s.isalnum()
s.isalpha()
s.isdecimal()

#Format
s1 = 'Olá {nome}, sua idade: {idade}.'.format(nome='Maria',idade=20)
print(s1)

