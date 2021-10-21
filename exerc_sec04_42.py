salario_base = float(input("Digite o salário base:"))
gratificacao = salario_base*0.05
salario_menosimposto = salario_base*0.93

salario_final = salario_menosimposto + gratificacao


print(f"O salário final é de {round(salario_final, 2)}")