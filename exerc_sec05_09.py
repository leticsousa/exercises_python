salario = float(input("Informe o salário:\n"))
prestacao = float(input("Informe o valor da prestação:\n"))

if prestacao > salario*0.2:
    print("Empréstimo não concedido.")

else:
    print("Empréstimo concedido.")
