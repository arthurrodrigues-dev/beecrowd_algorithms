n = int(input())

FIBONACCI = ((((1 + 5 ** 0.5) / 2) ** n) - (((1 - 5 ** 0.5) / 2)) ** n) / (5 ** 0.5)

print('{:.1f}'.format(FIBONACCI))