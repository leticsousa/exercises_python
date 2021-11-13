print("/ = divisão")
print('* = multiplicação')
print('- = subtração')
print('+ = adição')

operacao = input("Escolha uma das operações acima:\n")
num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

if operacao == "/":
    resultado = num1 / num2
    print("O resultado é", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é", resultado)

elif operacao == '+':
    resultado = num1 + num2
    print("O resultado é", resultado)

else:
    print("Operação não encontrada.Escolha uma das quatro opções de operações oferecidas.")
