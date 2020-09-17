lista_quadrado = []
lista_saida = []

for n in range(0, 5):
    entrada= input("Informe um número inteiro:")
    entrada= int(entrada)
    lista_quadrado.append(entrada)
    potenciacao = (entrada ** 2)
    lista_saida.append(potenciacao)

print(f"A lista dos números informados: {lista_quadrado}")
print(f"A lista dos números elevado ao quadrado: {lista_saida}")



