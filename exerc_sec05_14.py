trablab = float(input("Digite a nota do Trabalho de Laboratório (entre 0 e 10):\n"))
ava_sem = float(input("Digite a nota da Avaliação Semestral (entre 0 e 10):\n"))
exame_fin = float(input("Digite a nota do Exame final (entre 0 e 10):\n"))

media_pond = ((trablab*2) + (ava_sem*3) + (exame_fin*5)) / 10

if 0 <= media_pond <=2.9:
    print(f"Média final {media_pond}. Aluno reprovado.")

elif 3 <= media_pond <=4.9:
    print(f"Média final {media_pond}. Aluno em recuperação.")

else:
    print(f"Média final {media_pond}. Aluno aprovado.")
