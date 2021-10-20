valor_real = float(input("Digite o valor em real:"))
cotacao_dolar = float(input("Digite a cotação do dólar:"))

valor_dolar = valor_real*cotacao_dolar
print(f"O valor correspondente em dólares é de: {round(valor_dolar,2)}")