for i in range(1,7):
    nt1 = int(input(f"Digite a primeira nota do {i} aluno:"))
    nt2 = int(input(f"Digite a segunda nota do {i} aluno::"))
    med = (nt1+nt2)/2
    if med < 3:
        if i == 1:
            sit1 = "Reprovado"
        elif i == 2:
            sit2 = "Reprovado"
        elif i == 3:
            sit3 = "Reprovado"
        elif i == 4:
            sit4 = "Reprovado"
        elif i == 5:
            sit5 = "Reprovado"
        elif i == 6:
            sit6 = "Reprovado"
    elif med < 7:
        if i == 1:
            sit1 = "Exame"
        elif i == 2:
            sit2 = "Exame"
        elif i == 3:
            sit3 = "Exame"
        elif i == 4:
            sit4 = "Exame"
        elif i == 5:
            sit5 = "Exame"
        elif i == 6:
            sit6 = "Exame"
    elif med <= 10:
        if i == 1:
            sit1 = "Aprovado"
        elif i == 2:
            sit2 = "Aprovado"
        elif i == 3:
            sit3 = "Aprovado"
        elif i == 4:
            sit4 = "Aprovado"
        elif i == 5:
            sit5 = "Aprovado"
        elif i == 6:
            sit6 = "Aprovado"

print(f"O aluno 1 está {sit1}.")
print(f"O aluno 2 está {sit2}.")
print(f"O aluno 3 está {sit3}.")
print(f"O aluno 4 está {sit4}.")
print(f"O aluno 5 está {sit5}.")
print(f"O aluno 6 está {sit6}.")