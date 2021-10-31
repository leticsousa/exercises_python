import math

num = float(input("Informe um número:\n"))

if num > 0:
    quadrado = pow(num,2)
    print(f"O número elevado ao quadrado é {round(quadrado, 2)}.")
    raiz = math.sqrt(num)
    print(f"A raíz quadrada do número é {round(raiz,2)}.")
