n = int(input())

for i in range(n):
  v1, v2, v3 = map(float, input().split())
  media_ponderada = ((v1 * 2) + (v2 * 3) + (v3 * 5)) / 10
  print("{:.1f}".format(media_ponderada))
