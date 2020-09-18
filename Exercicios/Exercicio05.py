lista_palavras = []

for n in range(0, 5):
    lista_entrada= input("Informe uma palavra:")
    lista_palavras.append(lista_entrada)


foundMaxiWord = max(lista_palavras, key=len)

print(f"A maior palavra da lista informada é: {foundMaxiWord})