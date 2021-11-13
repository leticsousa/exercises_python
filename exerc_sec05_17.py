base_maior = float(input("Informe o valor da base maior:\n"))
base_menor = float(input("Informe o valor da base menor:\n"))
altura = float(input("Informe o valor da altura:\n"))

area_trap = ((base_maior + base_menor) * altura) / 2

if base_maior > 0 and base_menor > 0:
    print("A área do trapézio é", area_trap)

else:
    print("Valores inválidos. Digite valores >0.")
