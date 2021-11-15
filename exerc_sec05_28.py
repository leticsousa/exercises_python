x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))
z = int(input("Digite um valor para z: "))

print("Escolha a média a ser calculada:\n"
      "1 = Geométrica\n"
      "2 = Ponderada\n"
      "3 = Harmônica\n"
      "4 = Aritmética")

escolha = int(input("Escolha: "))

if escolha == 1:
    media_geo = (x * y * z) ** (1 / 3)
    print("A média geométrica é", round(media_geo, 2))

elif escolha == 2:
    media_pond = (x + 2 * y + 3 * z)/6
    print("A média ponderada é", round(media_pond, 2))

elif escolha == 3:
    media_harm = 1 / (1/x + 1/y + 1/z)
    print("A média harmômica é", round(media_harm, 2))

elif escolha == 4:
    media_art = (x + y + z)/3
    print("A média aritmética é", round(media_art, 2))

else:
    print("Operação inválida.")
