"""1"""

numero = 1
print(numero)

"""2"""

numero = 3.5
print(numero)

"""3"""

idade1 = int(input("Qual a sua idade?"))
idade2 = int(input("Qual a idade da sua mãe?"))
idade3 = int(input("Qual a idade do seu pai?"))

soma = idade1 + idade2 + idade3
print("A soma da idade de vocês é:", soma)


"""4"""

numero = float(2.5)

quadrado = numero*numero

print(quadrado)

"""5"""

numero = int(5)

resultado =numero/5

print(resultado)

"""6"""

temperaturaC = float(input("Digite a temperatura em graus Celsis:"))

conversao = temperaturaC*(9/5)+32

print(f"A temperatura em Fahrenheit é: {conversao}ºF")


"""7"""

temp_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit:"))

temp_celsius = 5*(temp_fahrenheit - 32)/9

print(f"A temperatura em graus Celsius é: {temp_celsius}ºC")

"""8"""

temp_kelvin = float(input("Digite a temperatura em graus Kelvin:"))

temp_celsius2 = temp_kelvin - 273.15

print(f"A temperatura em graus Celsius é: {temp_celsius2}ºC")

"""9"""

temp_celsius3 = float(input("Digite a temperatura em graus Celsius:"))

temp_kelvin2 = temp_celsius3 + 273.15

print(f"A temperatura em graus Kelvin é: {temp_kelvin2}ºK")

"""10"""

veloc_kh_h = float(input("Digite a velocidade em km/h:" ))

veloc_m_s = veloc_kh_h/3.6

print("A velocidade em m/s é", veloc_m_s)

"""11"""

veloc_ms = float(input("Digite a velocidade em m/s:" ))

veloc_kmh = veloc_ms*3.6

print("A velocidade em km/h é", veloc_kmh)


"""12"""

milhas = float(input("Digite a velocidade milhas:"))

veloc_kmh2 = 1.61 * milhas

print("A velocidade em km/h é", veloc_kmh2)