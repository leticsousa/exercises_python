peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em m): "))

imc= peso / (altura*altura)

if imc < 18.5:
    print(f"O IMC é {round (imc, 2)}: Abaixo do peso.")

elif 18.6 <= imc <= 24.9:
    print(f"O IMC é {round(imc, 2)}: Saudável.")

elif 25 <= imc <= 29.9:
    print(f"O IMC é {round(imc, 2)}: Peso em excesso.")

elif 30 <= imc <= 34.9:
    print(f"O IMC é {round(imc, 2)}: Obesidade Grau I.")

elif 35 <= imc <= 39.9:
    print(f"O IMC é {round(imc, 2)}: Obesidade Grau II - severa.")

elif imc >= 40:
    print(f"O IMC é {round(imc, 2)}: Obesidade Grau III - mórbida.")

else:
    print("Valores inválidos.")
