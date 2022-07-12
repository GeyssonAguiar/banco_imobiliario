from random import randint

class Jogador:
  def __init__(self, caracteristica):
    self.saldo = 300
    self.propriedades_compradas = []
    self.caracteristica = caracteristica


  def joga_dado(self):
    return randint(1,6)


  def comportamento(self, propriedade_selecionada):
    if self.caracteristica == 'impulsivo':
      return True

    elif self.caracteristica == 'exigente' and propriedade_selecionada['valor_aluguel'] > 50:
      return True
  
    elif self.caracteristica == 'cauteloso' and self.saldo - propriedade_selecionada['valor_venda'] > 80:
      return True 

    elif self.caracteristica == 'aleatório':
      return randint(0,1)


  
      