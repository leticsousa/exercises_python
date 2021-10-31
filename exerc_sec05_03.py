import math

num = float(input("Informe um número:\n"))

if num > 0:
    num = math.sqrt(num)
    print(round(num,2))

else:
    num = pow(num,2)
    print(round(num, 2))
