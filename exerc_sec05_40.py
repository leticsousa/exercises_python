custo_fabr = float(input("Digite o custo de fábrica em R$: "))

if custo_fabr <=12000:
    custo_cons = custo_fabr + (custo_fabr*0.05)
    print(f"O custo do consumidor será de R$ {round(custo_cons, 2)}.")

elif 12000 < custo_fabr <=25000:
    custo_cons = custo_fabr + (custo_fabr*0.1) + (custo_fabr*0.15)
    print(f"O custo do consumidor será de R$ {round(custo_cons, 2)}.")

else:
    custo_cons =custo_fabr + (custo_fabr*0.15) + (custo_fabr*0.2)
    print(f"O custo do consumidor será de R$ {round(custo_cons, 2)}.")
