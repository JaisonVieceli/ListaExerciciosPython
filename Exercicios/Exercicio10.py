
nome_time = input("Informe o Nome do Time:")
nome_time = str(nome_time)
numero_vitorias =input("Informe Quantas vitórias:")
numero_vitorias =int(numero_vitorias)
numero_empates =input("Informe Quantos empates:")
numero_empates =int(numero_empates)
numero_derrotas =input("Informe Quantas derrotas:")
numero_derrotas =int(numero_derrotas)

pontos_vitorias = numero_vitorias * 3
pontos_total = pontos_vitorias + numero_empates

print(f"Pontos do Time {nome_time}: O total de pontos é {pontos_total}")





