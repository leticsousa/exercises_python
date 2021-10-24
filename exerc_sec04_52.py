premio = float(input("Digite o valor do prêmio:\n"))
inv1 = float(input("Digite o investimento do apostador 1:\n"))
inv2 = float(input("Digite o investimento do apostador 2:\n"))
inv3 = float(input("Digite o investimento do apostador 3:\n"))

total_aposta = inv1 + inv2 + inv3

prop_inv1 = inv1/total_aposta
prop_inv2 = inv2/total_aposta
prop_inv3 = inv3/total_aposta

premio_inv1 = prop_inv1*premio
premio_inv2 = prop_inv2*premio
premio_inv3 = prop_inv3*premio

print(f"O prêmio do apostador 1 é: {round(premio_inv1, 2)}")
print(f"O prêmio do apostador 2 é: {round(premio_inv2, 2)}")
print(f"O prêmio do apostador 3 é: {round(premio_inv3, 2)}")

