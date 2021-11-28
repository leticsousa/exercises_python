dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano:" ))

if mes == 1 and mes == 3 and mes == 5 and mes == 7 and mes == 8 and mes == 10 and mes == 12:
    if 1 <= dia <= 31:
        print("Dia válido.")

    else:
        print("Dia inválido.")

elif mes == 4 and mes == 6 and == 9 and mes == 11:
    if 1 <= dia <= 30:
        print("Dia válido.")

    else:
        print("Dia inválido.")

elif mes == 2:
    if ano %400 == 0 or ano % 4 == 0 and ano %100 != 0:
        if 1 <= dia <= 29:
            print("Dia válido.")

        else:
            print("Dia inválido.")

        else:
        if 1 <= dia <= 28:
            print("Dia válido.")

        else:
            print("Dia inválido.")

else:
    print("Dia inválido.")

