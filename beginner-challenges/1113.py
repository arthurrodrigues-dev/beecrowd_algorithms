x, y = 0, 1

while x != y:
    x, y = input().split()
    x, y = int(x), int(y)
    if x > y:
        print("Decrescente")
    if x < y:
        print("Crescente")
