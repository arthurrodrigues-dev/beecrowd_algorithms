nome = input()
salario_fixo, total_vendas = float(input()), float(input())

total = salario_fixo + 15/100 * total_vendas
print("TOTAL = R$ {:.2f}".format(total))
