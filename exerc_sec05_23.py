ano = int(input("Digite o ano:"))

if ano % 400 == 0:
    print("Ano bissexto.")

elif ano % 4 == 0 and ano % 100 != 0:
    print("O ano é bissexto.")

else:
    print("O ano não é bissexto.")
