num = int(input("Digite um número inteiro entre 1 e 12:\n"))

mes = ['Janeiro',
       'Fevereiro',
       'Março',
       'Abril',
       'Maio',
       'Junho',
       'Julho',
       'Agosto',
       'Setembro',
       'Outubro',
       'Novembro',
       'Dezembro']

if 1 < num > 12:
    print('Esse mês não existe!')
else:
    print(f'O mês selecionado é: {mes[num - 1]}.')
