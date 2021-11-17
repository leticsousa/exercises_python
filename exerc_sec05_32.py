print("Escolha o código do lanche:\n"
     "Cachorro Quente = 100\n"
     "Bauru Simples = 101\n"
     "Bauru com Ovo = 102\n"
     "Hamburguer = 103\n"
     "Cheeseburguer = 104\n"
     "Suco = 105\n"
     "Refrigerante = 106\n")

cod_lanche = int(input("Código: "))
qtd = int(input("Quantidade: "))
valor_final = cod_lanche * qtd

if cod_lanche == 100:
    valor_final = 1.2 * qtd
    print(f"O valor final do pedido é de {round(valor_final, 2)} reais.")

elif cod_lanche == 101:
    valor_final = 1.3 * qtd
    print(f"O valor final do pedido é de {round(valor_final, 2)} reais.")

elif cod_lanche == 102:
    valor_final = 1.5 * qtd
    print(f"O valor final do pedido é de {round(valor_final, 2)} reais.")

elif cod_lanche == 103:
    valor_final = 1.2 * qtd
    print(f"O valor final do pedido é de {round(valor_final, 2)} reais.")

elif cod_lanche == 104:
    valor_final = 1.7 * qtd
    print(f"O valor final do pedido é de {round(valor_final, 2)} reais.")

elif cod_lanche == 105:
    valor_final = 2.2 * qtd
    print(f"O valor final do pedido é de {round(valor_final, 2)} reais.")

elif cod_lanche == 106:
    valor_final = 1 * qtd
    print(f"O valor final do pedido é de {round(valor_final, 2)} reais.")

else:
    print("Código incorreto.")
