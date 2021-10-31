diasemana = ['domingo',
             'segunda',
             'terça',
             'quarta',
             'quinta',
             'sexta',
             'sábado']

dia = int(input("Digite um número entre 1 e 7:"))

if 1 < dia > 7:
    print('Esse dia não existe')
else:
    print(f'O dia selecionado é: {diasemana[dia - 1]}.')
