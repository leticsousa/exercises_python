idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    print("Categoria Infantil A.")

elif 8 <= idade <= 10:
    print("Categoria Infantil B.")

elif 11 <= idade <= 13:
    print("Categoria Juvenil A.")

elif 14 <= idade <= 17:
    print("Categoria Juvenil B.")

else:
    print("Categoria Sênior.")
