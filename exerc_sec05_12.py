import math

num = int(input("Digite um número inteiro:"))

if num > 0:
    num = math.log(num, 10)
    print("O logarítimo desse número é", round(num,2))

else:
    print("Número inválido.")
