# Calculadora de Operações Matemáticas by Beatriz Wurthmann

import math

while True:
    print("\t Menu \n")
    print("A - Raiz Quadrada")
    print("B - Raiz Cúbica")
    print("C - Quadrado do número")
    print("D - Cubo do número")
    print("E - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "a":
        numero = float(input("Digite um número: "))
        resultado = math.sqrt(numero)
        print("A raiz quadrada de", numero, "é: ", resultado)
    elif opcao == "b":
        numero = float(input("Digite um número: "))
        resultado = numero ** (1/3)
        print("A raiz cúbica de", numero, "é: ", resultado)
    elif opcao == "c":
        numero = float(input("Digite um número: "))
        resultado = numero ** 2
        print("O quadrado de", numero, "é: ", resultado)
    elif opcao == "d":
        numero = float(input("Digite um número: "))
        resultado = numero ** 3
        print("O cubo de", numero, "é: ", resultado)
    elif opcao == "e":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")