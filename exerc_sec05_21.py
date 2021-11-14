print('Escolha uma das opções abaixo: \n 1 = soma de 2 números\n 2 = diferença entre dois números (maior pelo menor)\n 3 = produto entre dois números\n 4 = divisão entre dois números (denominador >0)')

opcao = int(input("Opção:\n"))
num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

if opcao == 1:
    resultado = num1 + num2
    print(f"A soma de {num1} + {num2} é {resultado}.")

elif opcao == 2 and num1 >= num2:
    resultado = num1 - num2
    print(f"A diferença entre {num1} e {num2} é de {resultado}.")

elif opcao == 2 and num2 >= num1:
    resultado = num2 - num1
    print(f"A diferença entre {num2} e {num1} é de {resultado}.")

elif opcao == 3:
    resultado = num1 * num2
    print(f"O produto de {num1} e {num2} é {resultado}.")

elif opcao == 4 and num2 > 0:
    resultado = num1/num2
    print(f"O resultado da divisão entre {num1} e {num2} é {resultado}.")

else:
    print("Opção inválida.")
