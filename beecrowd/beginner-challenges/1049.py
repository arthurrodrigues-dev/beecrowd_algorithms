dict = {
  'vertebrado': {
    'ave': {
      'carnivoro': 'aguia',
      'onivoro': 'pomba'
    },
    'mamifero': {
      'onivoro': 'homem',
      'herbivoro': 'vaca'
    }
  },
  'invertebrado': {
    'inseto': {
      'hematofago': 'pulga',
      'herbivoro': 'lagarta'
    },
    'anelideo': {
      'hematofago': 'sanguessuga',
      'onivoro': 'minhoca'
    }
  }
}

v_inv = input()
especie = input()
classificacao = input()

print(dict[v_inv][especie][classificacao])
