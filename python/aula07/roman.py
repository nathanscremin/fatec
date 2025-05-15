nrom = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}
reve = sorted(nrom, reverse = True)
def num_romanos(numero):
    rom = '' 
    for value in reve:
        while numero >= value:
            rom += reve.get(value)
            numero = numero - value
    return rom

assert num_romanos(42) == 'XLII'
assert num_romanos(300) == 'CCC'