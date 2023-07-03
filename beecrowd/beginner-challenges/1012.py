a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

area_triangulo = (a * c) / 2
area_circulo = 3.14159 * (c ** 2)
area_trapezio = ((a + b) / 2) * c
area_quadrado = b ** 2
area_retangulo = a * b

print("TRIANGULO: {:.3f}".format(area_triangulo))
print("CIRCULO: {:.3f}".format(area_circulo))
print("TRAPEZIO: {:.3f}".format(area_trapezio))
print("QUADRADO: {:.3f}".format(area_quadrado))
print("RETANGULO: {:.3f}".format(area_retangulo))

