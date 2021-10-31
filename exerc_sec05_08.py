nota1 = float(input("Informe a nota 1:\n"))
nota2 = float(input("Informe a nota 2:\n"))

if 0 <= nota1 <=10 and 0 <= nota2 <=10:
    media = (nota1 + nota2)/2
    print("A média das notas é", media)

else:
    print("Notas informadas não válidas. As notas devem estar entre 0 e 10. Tente novamente.")
