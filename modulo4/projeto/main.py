from models.jogador import Jogador
from models.jogadores import Jogadores
from models.jogo import Jogo

def main():
    num_jogadores = int(input("Quantos jogadores participarão? "))
    jogadores = Jogadores()

    for i in range(num_jogadores):
        nome = input(f"\nEntre com o nome do jogador {i + 1}: ")
        jogador = Jogador(nome)
        jogadores.adicionar_jogador(jogador)

    num_rodadas = int(input("Quantas rodadas você deseja jogar? "))
    jogo = Jogo(num_rodadas)
    jogo.simular(jogadores)
    jogadores.contabilizar_vitorias()
    jogadores.analisar()
    jogadores.exibir()

if __name__ == "__main__":
    main()