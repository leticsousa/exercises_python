n1 = float(input("Digite a primeira nota:\n"))
n2 = float(input("Digite a segunda nota:\n"))
n3 = float(input("Digite a terceira nota:\n"))

media_pond = (((n1*1) + (n2*1) + (n3*2)) / 4)*10

if media_pond > 60:
    print(f"Média final {media_pond}. Aluno aprovado!")

else:
    print(f"Aluno não aprovado. Média final {media_pond}.")
