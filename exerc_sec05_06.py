num1 = int(input("Informe o primeiro número:"))
num2 = int(input("Informe o segundo número:"))

if num1 > num2:
    print("O maior número é", num1)
    dif = num1 - num2
    print("A diferença entre os números é de", dif)

else:
    print("O maior número é", num2)
    dif = num2- num1
    print("A diferença entre os números é de", dif)
