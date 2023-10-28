class Jogo:
    
    def __init__(self, num_rodadas):
        self.num_rodadas = num_rodadas

    def simular(self, jogadores):
        for rodada in range(self.num_rodadas):
            print(f"\nRodada {rodada + 1}:")
            for jogador in jogadores:
                resultado = jogador.jogar_dado()
                print(f"O {jogador.nome} lançou o dado e obteve face {resultado}")

    def analisar(self, jogadores):
        campeao = jogadores.jogadores[0]
        empate = [j for j in jogadores.jogadores if j.vitorias == campeao.vitorias]
        if len(empate) > 1:
            print("\nHouve um empate entre os seguintes jogadores:")
            for jogador in empate:
                print(jogador.nome)
        else:
            print(f"\nO campeão é {campeao.nome}!")