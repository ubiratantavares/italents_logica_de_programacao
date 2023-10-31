import random

# criando os itens do jogo
def criar_itens():
    return ["pedra", "papel", "tesoura"]

# lendo o número de rodadas
def ler_numero_rodadas(mensagem):
    return int(input(f'{mensagem} '))

# selecionando um item pelo computador
def selecionar_item_maq(itens):
    return random.choice(itens)

# selecionando um item o usuario
def selecionar_item_user(itens):
    for i in range(len(itens)):
        print(f"{i + 1} - {itens[i]}")
    idx = int(input("Usuário, escolha um número: "))
    if itens[idx - 1] not in itens:
        print("Escolha inválida. Tente novamente.")
        selecionar_item_user(itens)    
    return itens[idx - 1]

# verificando o vencedor da rodada
def verificar_vencedor(itens, user, maq):
    if user == maq:
        return "Empate"
    elif (user == itens[0] and maq == itens[2]) or (user == itens[1] and maq == itens[0]) or (user == itens[2] and maq == itens[1]):
        return "Usuário"
    else:
        return "Computador"

# exibindo o resultado da rodada
def exibir_resultado_da_rodada(i, user, maq, result):
    print(f"\nUsuário escolheu: {user}")
    print(f"Computador escolheu: {maq}")
    print(f"\nVencedor da rodada {i + 1}: {result}\n")

# iniciar o jogo
def jogar(num_rodadas):
    user_vitorias = 0
    maq_vitorias = 0
    for i in range(num_rodadas):
        print(f"\nRodada {i + 1}\n")
        # Em cada rodada, o programa deve pedir que o usuário escolha entre pedra, papel e tesoura: requisito atendido
        select_user = selecionar_item_user(criar_itens())
        # O programa deve decidir aleatoriamente a escolha do computador: requisito atendido
        select_maq = selecionar_item_maq(criar_itens())
        # Mostrar na tela a jogada do usuário e a do computador, bem como o resultado da rodada (vencedor ou empate)
        resultado = verificar_vencedor(criar_itens(),  select_user, select_maq)
        if resultado == "Usuário":
            user_vitorias += 1
        if resultado == "Computador":
            maq_vitorias += 1
        exibir_resultado_da_rodada(i, select_user, select_maq, resultado)        
    return user_vitorias, maq_vitorias

# exibindo o resultado das rodadas
def exibir_resultado_das_rodadas(num_rodadas, user_vitorias, maq_vitorias):
    print(f"\n*** Término das {num_rodadas} rodadas ***")
    print("\nResumo dos resultados:")
    # No final das rodadas, o programa deve mostrar quantas rodadas cada jogador ganhou: requisito atendido
    if user_vitorias == 0:
        print(f"Você não ganhou nenhuma rodada.")
    elif user_vitorias == 1:
        print(f"Você ganhou {user_vitorias} rodada.")
    else:
        print(f"Você ganhou {user_vitorias} rodadas.")

    if maq_vitorias == 0:
        print(f"Computador não ganhou nenhuma rodada.")     
    elif maq_vitorias == 1:
        print(f"Computador ganhou {maq_vitorias} rodada.")
    else:
        print(f"Computador ganhou {maq_vitorias} rodadas.")

    if user_vitorias > maq_vitorias:
        print("\nVocê é o grande campeão!")
    elif maq_vitorias > user_vitorias:
        print("\nComputador é o grande campeão!")
    else:
        print("\nDeu empate!")

# perguntando ao usuário se deseja jogar novamente o jogo
def jogar_novamente():
    # Perguntar se o usuário quer jogar novamente: requisito atendido       
    resposta = input("\nDeseja jogar novamente (sim/não)? ").lower()
    if resposta == 'sim':
        return True
    return False
