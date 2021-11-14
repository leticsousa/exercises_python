a = int(input("Informe um valor do lado A do triângulo:\n"))
b = int(input("Informe um valor do lado B do triângulo:\n"))
c = int(input("Informe um valor do lado C do triângulo:\n"))

while b + c < a:
    print("O valor inserido em 'A' não pode ser maior que a soma de 'B' + 'C', digite novamente")
    a = int(input("Informe um valor do lado A do triângulo: \n"))
    b = int(input("Informe um valor do lado B do triângulo: \n"))
    c = int(input("Informe um valor do lado C do triângulo: \n"))

while a + c < b:
    print("O valor inserido em 'B' não pode ser maior que a soma de 'A' + 'C', digite novamente")
    a = int(input("DInforme um valor do lado A do triângulo: \n"))
    b = int(input("Informe um valor do lado B do triângulo: \n"))
    c = int(input("Informe um valor do lado C do triângulo: \n"))

while a + b < c:
    print("O valor inserido em 'C' não pode ser maior que a soma de 'A' + 'B', digite novamente")
    a = int(input("Informe um valor do lado A do triângulo: \n"))
    b = int(input("Informe um valor do lado B do triângulo: \n"))
    c = int(input("Informe um valor do lado C do triângulo: \n"))

if a == b == c:
    print("Triângulo equilátero.")

elif a == b or b == c:
    print("Triângulo isósceles.")

else:
    print("Triângulo escaleno.")
