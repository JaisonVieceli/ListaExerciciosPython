lista_elementos_1 = ["Douglas", "Anderson", "Libório", "Maicon", "Prefeito Géri"]
lista_elementos_2 = ["Douglas", "Maicon", "Libório"]

lista_diferenca = list(set(lista_elementos_1)- set(lista_elementos_2))

print(f'Os elementos que não estão em ambas as listas são: {lista_diferenca}')

# A lista resultante diferente do enunciado, vai ser [Prefeito Géri, Anderson]