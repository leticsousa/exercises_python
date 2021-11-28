valor_venda = float(input("Digite o valor da venda mensal em R$: "))

if valor_venda >= 100000:
    comissao = 700 + (valor_venda*0.16)
    print(f"O valor da comissão é R$ {round(comissao, 2)}.")

elif 80000 <=valor_venda < 100000:
    comissao = 650 + (valor_venda*0.14)
    print(f"O valor da comissão é R$ {round(comissao, 2)}.")

elif 60000 <=valor_venda < 80000:
    comissao = 600 + (valor_venda*0.14)
    print(f"O valor da comissão é R$ {round(comissao, 2)}.")

elif 40000 <=valor_venda < 60000:
    comissao = 550 + (valor_venda*0.14)
    print(f"O valor da comissão é R$ {round(comissao, 2)}.")

elif 20000 <=valor_venda < 40000:
    comissao = 500 + (valor_venda*0.14)
    print(f"O valor da comissão é R$ {round(comissao, 2)}.")

elif valor_venda < 20000:
    comissao = 400 + (valor_venda*0.14)
    print(f"O valor da comissão é R$ {round(comissao, 2)}.")

else:
    print("Valores inválidos.")
