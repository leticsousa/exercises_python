num = int(input("Informe um número inteiro entre 0 e 999:\n"))
num1 = str(num)

if 0<= num <= 9:
    soma = int(num1[0])
    print("A soma de seus algarismo é de", soma)

elif 10<=num<=99:
    soma = int(num1[0]) + int(num1[1])
    print("A soma de seus algarismo é de", soma)

elif 100<=num<=999:
    soma = int(num1[0])+ int(num1[1]) + int(num1[2])
    print("A soma de seus algarismo é de", soma)

else:
    print("Número inválido.")
