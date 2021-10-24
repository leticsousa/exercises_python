c = float(input("Comprimento do terreno em m:\n"))
l = float(input("Largura do terreno em m:\n"))
p = float(input("Preço do metro de tela:\n"))

custo_cercamento = (2*c + 2*l) * p

print("O preço para cercar um terreno nessas dimensões é de", custo_cercamento)