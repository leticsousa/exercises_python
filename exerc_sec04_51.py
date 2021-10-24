x1 = int(input('Informe a coordenada x1:'))
y1 = int(input('Informe a coordenada y1:'))

distancia = int((((0 - x1) ** 2) + ((0 - y1) ** 2)) ** (1 / 2))

print(f'A distância entre a origem (0,0) e as coordenadas informadas ({x1},{y1}) é: {distancia}')