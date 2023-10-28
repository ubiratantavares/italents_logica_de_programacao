import random

def ler(mensagem):
    return int(input(mensagem))

def jogar():
    return random.randint(1, 6)

def criar_jogador(nome):
    return {'nome': nome, 'resultados': [], 'vitorias': 0}

def criar_jogadores(num_jogadores):
    jogadores = []
    for i in range(num_jogadores):
        nome = input(f"\nEntre com o nome do jogador {i+1}: ")
        jogador = criar_jogador(nome)
        jogadores.append(jogador)
    return jogadores

def simular(num_rodadas, jogadores):
    for rodada in range(num_rodadas):
        print(f"\nRodada {rodada + 1}:")
        for jogador in jogadores:
            resultado = jogar()
            jogador['resultados'].append(resultado)
            print(f"O {jogador['nome']} lançou o dado e obteve face {resultado}")

def contabilizar(jogadores):
    for jogador in jogadores:
        jogador['vitorias'] = jogador['resultados'].count(6) 
    # ordenando os jogadores pelo número de vitórias
    jogadores.sort(key=lambda jogador: jogador['vitorias'], reverse=True) # Supondo
    
def exibir(jogadores):
    print("\nResultado Final:")
    for jogador in jogadores:
        print(f"O {jogador['nome']} venceu {jogador['vitorias']} rodadas.")

def analisar(jogadores):
    campeao = jogadores[0]
    empate = [j for j in jogadores if j['vitorias'] == campeao['vitorias']]
    if len(empate) > 1:
        print("\nHouve um empate entre os seguintes jogadores:")
        for jogador in empate:
            print(jogador['nome'])
    else:
        print(f"\nO campeão é {campeao['nome']}!")