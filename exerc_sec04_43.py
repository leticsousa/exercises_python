valor_total_compra = float(input("Valor total da compra:\n"))

valor_a_vista = valor_total_compra*0.9
valor_parcel = valor_total_compra/3
comissao_a_vista = valor_a_vista*0.05
comissao_parcel = valor_total_compra*0.05

print("O total a pagar à vista com 10% de desconto é", round(valor_a_vista, 2))
print("O total a pagar parcelado em 3x sem juros é", round(valor_parcel, 2))
print("Comissão da venda à vista (5%):", round(comissao_a_vista,2))
print("Comissão da venda parcelada em 3x sem juros:", round(comissao_parcel, 2))