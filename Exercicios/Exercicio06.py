qtde_sequencias = input("Informe quantas sequências deseja:")
qtde_sequencias = int(qtde_sequencias)
termo1 = 0
termo2 = 1
contador = 3
print(f"Inicio {termo1}  - {termo2}", end = '')
while contador <= qtde_sequencias:
    termo3 = termo1 + termo2
    print(f" - {termo3} ", end = '')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print("Fim")