altura_degrau = float(input("Digite a altura do degrau em m:\n"))
altura_desejada = float(input("Digite a altura que o usuário quer alcançar em m:\n"))

degraus_neces = altura_desejada/altura_degrau

print("O número de degraus que o usuário deve subir para alcançar a altura desejada é", round(degraus_neces, 2))
