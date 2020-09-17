lista_ordem = []

for n in range(0, 5):
    lista_entrada= input("Informe um número inteiro ou com ponto flutuante:")
    lista_entrada= float(lista_entrada)
    lista_ordem.append(lista_entrada)

soma_numeros = sum(lista_ordem)
qtde_numeros = len(lista_ordem)
resultado = soma_numeros / qtde_numeros

print(f"A lista informada: {lista_ordem}")
print(f"A média dos números informados é: {resultado}")