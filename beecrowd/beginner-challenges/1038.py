snacks = {
  1: "Cachorro Quente",
  2: "X-Salada",
  3: "X-Bacon",
  4: "Torrada Simples",
  5: "Refrigerante"
}

prices = {
  "Cachorro Quente": 4.00,
  "X-Salada": 4.50,
  "X-Bacon": 5.00,
  "Torrada Simples": 2.00,
  "Refrigerante": 1.50
}

def get_price(code, qtde):
  price = prices[snacks[code]] * qtde
  return price
  
code, qtde = map(float, input().split())
total = get_price(code, qtde)
print("Total: R$ {:.2f}".format(total))

  
