altura = float(input("Digite a altura em m: "))
peso = float(input("Digite o peso em kg: "))

if altura <1.2 and peso < 60:
    print("Classificação A.")

elif altura <1.2 and 60 <= peso <= 90:
    print("Classificação D.")

elif altura <1.2 and peso > 90:
    print("Classificação G.")

elif 1.2 <= altura <= 1.7 and peso < 60:
    print("Classificação B.")

elif 1.2 <= altura <= 1.7 and 60 <= peso <= 90:
    print("Classificação E.")

elif 1.2 <= altura <= 1.7  and peso > 90:
    print("Classificação H.")

elif altura > 1.7 and peso < 60:
    print("Classificação C.")

elif altura > 1.7 and 60 <= peso <= 90:
    print("Classificação F.")

elif altura > 1.7  and peso > 90:
    print("Classificação I.")

else:
    print("Dados inválidos.")
