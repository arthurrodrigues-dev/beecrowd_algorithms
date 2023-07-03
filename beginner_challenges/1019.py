n = int(input())

minutos = n // 60
n %= 60
horas = minutos // 60
minutos -= horas * 60

print(horas, ":", minutos, ":", n, sep="")
