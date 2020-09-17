ano_atual =input("Informe o ano:")
ano_atual =int(ano_atual)


a = (19 * (ano_atual % 19) + 24) % 30
b = (2 * (ano_atual % 4) + 4 * (ano_atual % 7) + 6 * a + 5) % 7
c = a + b

if c > 9:
    dia = c - 9
    print(f"A Pascoa vai acontecer no mês de Abril no dia: {dia} ")
else:
    dia = c + 22
    print(f"A Pascoa vai acontecer no mês de Março no dia: {dia} ")

