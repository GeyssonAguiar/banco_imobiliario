from random import choice
from jogador import Jogador
from propriedade import Propriedade
from tabuleiro import Tabuleiro

class Jogo:
  def __init__(self, jogadores, propriedade, tabuleiro):
    self.jogadores = jogadores
    self.propriedade = propriedade
    self.tabuleiro = tabuleiro
    self.rodadas = 0


  def estatisticas(self):
    pass

  def sorteia_ordem_jogadores(self):
    for _ in range(len(self.jogadores)):
      sorteado = choice(self.jogadores)
      self.jogadores.remove(sorteado)
      self.jogadores.append(sorteado)

  def verifica_game_over(self):
    if self.jogadores == 1:
      print('Fim de jogo')
      return True

    elif self.rodadas > 1000:
      print('Fim de jogo')
      return True

  def verifica_saldo(self, jogador):
    if jogador.saldo < 0:
      self.jogadores.remove(jogador)
      print('Você está fora')

  def verifica_jogada(self, jogador, dados):
    propriedade_selecionada = self.propriedade.propriedades[dados]
    comportamento = jogador.comportamento(propriedade_selecionada)
    
    if not propriedade_selecionada['comprada'] and propriedade_selecionada['valor_venda'] <= jogador.saldo and comportamento:
      jogador.saldo -= propriedade_selecionada['valor_venda']
      jogador.propriedades_compradas.append(propriedade_selecionada)
      propriedade_selecionada['comprada'] = jogador
      print(jogador.caracteristica, ' Comprou ', propriedade_selecionada, jogador.saldo)

    elif propriedade_selecionada['comprada'] and propriedade_selecionada['valor_aluguel'] <= jogador.saldo and comportamento:
      jogador.saldo = jogador.saldo - propriedade_selecionada['valor_aluguel']
      jogador_proprietario = propriedade_selecionada['comprada']
      jogador_proprietario.saldo += propriedade_selecionada['valor_aluguel']
      print(jogador.caracteristica, ' Pagou aluguel ', propriedade_selecionada, jogador.saldo,' - ',jogador_proprietario.saldo)

  def cria_jogo(self):
    self.sorteia_ordem_jogadores()
  
    for i in range(1000):
      print('Rodada ', i, '\n\n')
      for jogador in self.jogadores:
        dados = jogador.joga_dado()
        
        jogador.saldo += self.tabuleiro.andar_casas(jogador, dados)
        self.verifica_jogada(jogador, dados)  
        self.verifica_saldo(jogador)
        
    if self.verifica_game_over():
      print('Fim de jogo')

      

jogo = Jogo([Jogador('impulsivo'), Jogador('exigente'), Jogador('cauteloso'), Jogador('aleatório')], Propriedade(), Tabuleiro())  
jogo.cria_jogo()







