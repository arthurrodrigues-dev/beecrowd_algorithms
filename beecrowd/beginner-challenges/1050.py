ddd = {
  61: "Brasilia",
  71: "Salvador",
  11: "Sao Paulo",
  21: "Rio de Janeiro",
  32: "Juiz de Fora",
  19: "Campinas",
  27: "Vitoria",
  31: "Belo Horizonte"
}

def get_ddd(n):
  if ddd.get(n) == None:
    return "DDD nao cadastrado"
  else: 
    return ddd[n]

v_ddd = int(input())
print(get_ddd(v_ddd))
