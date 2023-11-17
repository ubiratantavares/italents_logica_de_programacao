from subrotinas import *


while True:
    # Perguntar ao usuário quantas rodadas deseja jogar: requisito atendido
    num_rodadas = ler_numero_rodadas("Quantas rodadas deseja jogar?")
    user_vitorias, computer_vitorias = jogar(num_rodadas)
    exibir_resultado_das_rodadas(num_rodadas, user_vitorias, computer_vitorias)
    if not jogar_novamente():
        break