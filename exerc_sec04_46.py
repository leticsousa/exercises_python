numero = int(input("Número inteiro positivo de três dígitos:\n"))

while numero < 100 or numero > 999:
    numero = int(input("Número inteiro positivo de três dígitos:\n"))


numero = str(numero)
reverse = numero[::-1]

print(f"O numero digitado ao contrário é: {reverse}")