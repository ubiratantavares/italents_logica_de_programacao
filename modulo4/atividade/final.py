import random


def jogar_dado():
    return random.randint(1, 6)


def main():
    # perguntando ao usuário quantas rodadas
    num_rodadas = int(input("Quantas rodadas voce deseja jogar? "))

    # perguntando quantos jogadores vao participar do jogo
    num_jogadores = int(input("Quantos jogadores vao participar do jogo? "))

    # criando a lista para armazenar os dados de cada jogador e os seus resultados
    jogadores = []

    # iterando para criar um dicionário com o nome e os resultados para cada jogador
    for i in range(num_jogadores):
        nome_jogador = input(f"Digite o nome do jogador {i + 1}: ")
        jogador = {"nome": nome_jogador, "resultados": []}
        jogadores.append(jogador)

    # iterando para cada rodada do jogo
    for rodada in range(num_rodadas):
        print(f"\nRodada {rodada + 1}:")

        # iterando para que cada jogador jogue a rodada
        for jogador in jogadores:
            # jogando e obtendo o resultado do dado
            resultado = jogar_dado()
            # armazenando resultado do dado em resultados
            jogador["resultados"].append(resultado)
            print(f"{jogador['nome']} sorteou {resultado}.")

    for jogador in jogadores:
        vitorias = 0
        for valor in jogador['resultados']:
            if valor == 6:
                vitorias += 1
        jogador['vitorias'] = vitorias

        # ordenando cada dicionário da lista em ordem decrescente da quantidade de vitórias.
    jogadores.sort(key=lambda x: x["vitorias"], reverse=True)

    # exibindo o resultado final
    print("\nResultado Final:\n")
    for i in range(0, len(jogadores)):
        if jogadores[i]['vitorias'] > 0:
            print(
                f"{jogadores[i]['nome']} obteve {jogadores[i]['vitorias']} vitorias.")

    nome = jogadores[0]['nome']
    vitorias = jogadores[0]['vitorias']

    for i in range(1, len(jogadores)):
        if jogadores[i]['vitorias'] > vitorias:
            vitorias = jogadores[i]['vitorias']
            nome = jogadores[i]['nome']
        if jogadores[i]['vitorias'] == vitorias:
            print(f"{jogadores[i]['nome']} empatou com {nome}.")
            vitorias = jogadores[i]['vitorias']
            nome = ""

    if nome != "":
        print(f"\nO vencedor é {nome}.")
    else:
        print("\nSem vencedor.")


if __name__ == "__main__":
    main()
