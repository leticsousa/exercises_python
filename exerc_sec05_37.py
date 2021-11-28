import math

print('Este programa recebe o horário de chegada e o horário de partida, na forma (h, min), de um veículo e '
      'retorna o valor que o usuário deve pagar.')

print('Horário de chegada')
hora_chegada = int(input('Hora: '))
min_chegada = int(input('Minuto: '))

tempo_min_chegada = hora_chegada * 60 + min_chegada  # total de minutos correspondentes à hora de entrada

print('Horário de saída')
hora_saida = int(input('Hora: '))
min_saida = int(input('Min: '))

tempo_min_saida = hora_saida * 60 + min_saida  # total de minutos correspondentes à hora de saída

tempo_h = math.ceil((tempo_min_saida - tempo_min_chegada) / 60)  # tempo de permanência em horas, arredondando pra cima
qtd_h = math.floor((tempo_min_saida - tempo_min_chegada) / 60)  # tempo de permanência real em horas
qtd_min = tempo_min_saida - tempo_min_chegada - qtd_h * 60  # tempo de permanência em minutos, descontando as horas

taxa = 0  # variável que carrega o valor da taxa

if 1 <= tempo_h <= 2:
    taxa = 1
elif 3 <= tempo_h <= 4:
    taxa = 1.4
elif 5 <= tempo_h:
    taxa = 2
else:
    pass

pagar = round(tempo_h * taxa, 2)  # valor a ser pago, arredondado em duas casas

print(f'O valor a ser pago é de R$ {pagar}.', end=' ')

if qtd_h >= 1:  # exibição do tempo de permanência
    print(f'Tempo de permanência: {qtd_h}h e {qtd_min}min.')
else:
    print(f'Tempo de permanência: {qtd_min}min')
