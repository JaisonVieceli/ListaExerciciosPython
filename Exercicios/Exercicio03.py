numero_primeiro =input("Informe um número:")
numero_primeiro =int(numero_primeiro)
numero_segundo =input("Informe um número:")
numero_segundo =int(numero_segundo)
numero_terceiro =input("Informe um número:")
numero_terceiro =int(numero_terceiro)

if(numero_primeiro == numero_segundo):
    if(numero_segundo == numero_terceiro):
        resultado = (numero_primeiro**3)
        print(f"O resultado desta operação foi elevado a terceira potência: {resultado}")

else:
    resultado = numero_primeiro + numero_segundo + numero_terceiro
    print(f"O resultado desta soma é: {resultado}")
