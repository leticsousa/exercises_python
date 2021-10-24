num = int(input("Digite um numero inteiro de 4 dígitos (de 1000 a 9999):\n"))

while num < 1000 or num > 9999:
    print("Digite um numero inteiro de 4 dígitos (de 1000 a 9999):\n")
    num = int(input())

print(f"O primeiro digito é {str(num)[0]}")
print(f"o segundo digito é {str(num)[1]}")
print(f"O terceiro digito é {str(num)[2]}")
print(f"O quarto digito é {str(num)[3]}")


