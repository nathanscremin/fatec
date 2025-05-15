sal = float(input("Insira seu salário bruto:"))

if sal < 2112:
    sall = 0
    print("Isento.")
elif sal < 2826.65:
    sall = (sal * (7.5/100)) - 158.40
elif sal < 3751.05:
    sall = (sal * (15/100)) - 370.40
elif sal < 4664.68:
    sall = (sal * (22.5/100)) - 651.73
elif sal >= 4664.68:
    sall = (sal * (27.5/100)) - 884.96

print(f"Imposto de renda: {sall}")