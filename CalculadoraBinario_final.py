while True:
    print("\t\t\t ** Calculadora De Binários ** \n\n ")
    print("[+] Soma")
    print("[-] Subtração")
    print("[*] Multiplicação")
    print("[/] Divisão")
    print("[0] Sair")
    opcao = input("Digite a opção desejada: ")
   
   # Soma
    if opcao == '+':
        try:
            bin1 = input("Digite o primeiro valor binário: ")
            num1 = int(bin1, 2)
            bin2 = input("Digite o segundo valor binário: ")
            num2 = int(bin2, 2)
        except ValueError:
            print("Valor inválido. Digite apenas números binários (0 ou 1).")
            continue
        
        result = num1 + num2
        print(f"{bin1} + {bin2} = {bin(result)[2:]}")
    
    # Subtracao
    elif opcao == '-':
        try:
            bin1 = input("Digite o primeiro valor binário: ")
            num1 = int(bin1, 2)
            bin2 = input("Digite o segundo valor binário: ")
            num2 = int(bin2, 2)
        except ValueError:
            print("Valor inválido. Digite apenas números binários (0 ou 1).")
            continue
        
        result = num1 - num2
        print(f"{bin1} - {bin2} = {bin(result)[2:]}")
    
    # Multiplicacao
    elif opcao == '*':
        try:
            bin1 = input("Digite o primeiro valor binário: ")
            num1 = int(bin1, 2)
            bin2 = input("Digite o segundo valor binário: ")
            num2 = int(bin2, 2)
        except ValueError:
            print("Valor inválido. Digite apenas números binários (0 ou 1).")
            continue
        
        result = num1 * num2
        print(f"{bin1} * {bin2} = {bin(result)[2:]}")
   
   # Divisao
    elif opcao == '/':
        try:
            bin1 = input("Digite o primeiro valor binário: ")
            num1 = int(bin1, 2)
            bin2 = input("Digite o segundo valor binário: ")
            num2 = int(bin2, 2)
            
            if num2 == 0:
                raise ZeroDivisionError
            
        except ValueError:
            print("Valor inválido. Digite apenas números binários (0 ou 1).")
            continue
        except ZeroDivisionError:
            print("Não é possível realizar divisão por 0!")
            continue
        
        result = num1 // num2
        print(f"{bin1} / {bin2} = {bin(result)[2:]}")
    
    #Sair
    elif opcao == '0':
        print(" \t\t\t A Calculadora está desligando... bye \n\n")
        break
    else:
        if opcao != '0':
            print("Opção inválida! Digite um dos valores listados acima.")

#By Beatriz Wurthmann