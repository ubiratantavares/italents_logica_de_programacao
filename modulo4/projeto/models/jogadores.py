from models.jogador import Jogador

class Jogadores:
    
    def __init__(self):
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def contabilizar_vitorias(self):
        for jogador in self.jogadores:
            jogador.vitorias = jogador.resultados.count(6)
        self.jogadores.sort(key=lambda jogador: jogador.vitorias, reverse=True)