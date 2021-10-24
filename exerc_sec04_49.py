from datetime import datetime
from datetime import timedelta

inicio = input('Informe o horário de início do experimento, no formado HH:MM:SS: ')

inicio = datetime.strptime(inicio, '%H:%M:%S')

segundos = int(input('Informe a duração do experimento em segundos: '))

hora_final = inicio + timedelta(seconds=segundos)
print(f'A hora final do experimento foi: {hora_final.time()}')