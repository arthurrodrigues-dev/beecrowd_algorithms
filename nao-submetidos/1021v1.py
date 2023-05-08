n = float(input())

c100 = n // 100
resto = n % 100

c50 = resto // 50
resto %= 50

c20 = resto // 20
resto %= 20

c10 = resto // 10
resto %= 10

c5 = resto // 5
resto %= 5

c2 = resto // 2
resto %= 2

m1 = resto // 1
resto %= 1

m50 = resto // 0.5
resto %= 0.5

m25 = resto // 0.25
resto %= 0.25

m10 = resto // 0.1
resto %= 0.1

m5 = resto // 0.05
resto %= 0.05

m01 = resto // 0.01
resto %= 0.01

print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00".format(c100))
print("{:.0f} nota(s) de R$ 50.00".format(c50))
print("{:.0f} nota(s) de R$ 20.00".format(c20))
print("{:.0f} nota(s) de R$ 10.00".format(c10))
print("{:.0f} nota(s) de R$ 5.00".format(c5))
print("{:.0f} nota(s) de R$ 2.00".format(c2))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00".format(m1))
print("{:.0f} moeda(s) de R$ 0.50".format(m50))
print("{:.0f} moeda(s) de R$ 0.25".format(m25))
print("{:.0f} moeda(s) de R$ 0.10".format(m10))
print("{:.0f} moeda(s) de R$ 0.05".format(m5))
print("{:.0f} moeda(s) de R$ 0.01".format(m01))

