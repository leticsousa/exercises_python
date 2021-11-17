preco = float(input("Informe o valor para saber o aumento: "))
aumento = 0

if preco < 50:
    aumento = preco * 1.05
    print(f"Valor com aumento: {round(aumento, 2)}")
elif 50 <= preco <= 100:
    aumento = preco * 1.10
    print(f"Valor com aumento: {round(aumento, 2)}")
elif preco > 100:
    aumento = preco * 1.15
    print(f"Valor com aumento: {round(aumento, 2)}")
else:
    print("Valores inválidos.")

if aumento < 80:
    print("Barato")
elif 80 <= aumento <= 120:
    print("Normal")
elif 120 <= aumento <= 200:
    print("Caro")
elif aumento > 200:
    print("Muito caro")
else:
    print("Valores inválidos.")
