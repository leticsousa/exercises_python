valorhora_reais = int(input("Valor da hora trabalhada em reais:"))
horas_trab_mes = int(input("Dias trabalhados no mês:"))

salario_pago = (valorhora_reais * horas_trab_mes) * (1.1)

print(f"O salário total é de {round(salario_pago, 2)} reais")