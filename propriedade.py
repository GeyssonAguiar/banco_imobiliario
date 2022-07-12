from random import randint

class Propriedade:
  def __init__(self):
    self.propriedades = \
      [
        {f'propriedade':numeral,
          'valor_venda':randint(1,100), 
          'valor_aluguel':randint(1,100),
          'comprada':False
        } for numeral in range(21)
      ]


    

