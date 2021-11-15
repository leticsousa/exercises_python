valor = float(input("Informe o valor do produto sem imposto: "))
print("Informe o estado de destino do produto:\n"
      "1- MG \n"
      "2- SP \n"
      "3- RJ \n"
      "4- MS \n")

opcao = int(input("Opção: "))

if opcao == 1:
    valor_final = valor*1.07
    print("O valor do produto com imposto é", round(valor_final, 2))

elif opcao == 2:
    valor_final = valor * 1.12
    print("O valor do produto com imposto é", round(valor_final, 2))

elif opcao == 3:
    valor_final = valor * 1.15
    print("O valor do produto com imposto é", round(valor_final, 2))

elif opcao == 4:
    valor_final = valor * 1.08
    print("O valor do produto com imposto é", round(valor_final, 2))

else:
    print("Opção selecionada inválida.")
