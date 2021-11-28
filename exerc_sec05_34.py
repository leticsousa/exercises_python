faltas = int(input("Digite o número de faltas: "))
nota = float(input("Digite o nota: "))

if 9 <= nota <= 10 and faltas <= 20:
    print("Conceito: A.")

elif 9 <= nota <= 10 and faltas > 20:
    print("Conceito: B.")

elif 7.5 <= nota < 9 and faltas <= 20:
    print("Conceito: B")

elif 7.5 <= nota < 9 and faltas > 20:
    print("Conceito: C")

elif 5 <= nota < 7.5 and faltas <= 20:
    print("Conceito: C")

elif 5 <= nota < 7.5 and faltas > 20:
    print("Conceito: D")

elif 4 <= nota < 5 and faltas <= 20:
    print("Conceito: D")

elif 4 <= nota < 5 and faltas > 20:
    print("Conceito: E")

elif 0 <= nota < 4 and faltas <= 20:
    print("Conceito: E")

elif 0 <= nota < 4 and faltas > 20:
    print("Conceito: E")

else:
    print("Dados inválidos.")
