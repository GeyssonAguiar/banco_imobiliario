class Tabuleiro:
  def __init__(self):
    self.casas_tabuleiro = {x:[] for x in range(1, 21)}


  def posicao_tabuleiro(self, jogador):
    posicao = 0
    for casa in self.casas_tabuleiro: 
      if jogador in self.casas_tabuleiro[casa]:
        posicao = casa
      
    return posicao
      
      
  def andar_casas(self, jogador, dados):
    posicao_anterior = self.posicao_tabuleiro(jogador)
    posicao_atual = posicao_anterior + dados
    credito = 0


    if posicao_atual > 20:
      posicao_atual = posicao_atual - 20
      credito = 100
      print('Ganhou crédito')

    self.casas_tabuleiro[posicao_atual].append(jogador)
  
    if posicao_anterior > 0: 
      self.casas_tabuleiro[posicao_anterior].remove(jogador)

    print('\n', self.casas_tabuleiro)

    return credito



