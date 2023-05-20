class Golpe:
  def __init__(self, ataque, defesa, nivel):
    self.ataque = ataque
    self.defesa = defesa
    self.nivel = nivel
    self.valor_golpe = 0
    
  def setValorGolpe(self):
    if self.nivel % 2 == 0:
      self.valor_golpe = ((self.ataque + self.defesa) / 2) + bonus_aplicado
    else:
      self.valor_golpe = (self.ataque + self.defesa) / 2

    return self.valor_golpe


def novo_golpe(ataque, defesa, nivel):
  golpe = Golpe(ataque, defesa, nivel)
  golpe.setValorGolpe()
  golpes_jogadores.append(golpe.setValorGolpe())

def verifica_ganhador(lista_golpes):
  for i in range(len(lista_golpes)):
    valor1 = lista_golpes[i]
    valor2 = lista_golpes[i + 1]
    
    if valor1 == valor2:
      return "Empate"
    elif valor1 > valor2:
      return "Dabriel"
    else:
      return "Guarte"

golpes_jogadores = [] * 2
num_instancias = int(input())
for i in range(num_instancias):
  bonus_aplicado = int(input())
  for j in range(2):
    ataque, defesa, nivel = map(int, input().split())
    novo_golpe(ataque, defesa, nivel)
  print(verifica_ganhador(golpes_jogadores))
  golpes_jogadores = [] * 2