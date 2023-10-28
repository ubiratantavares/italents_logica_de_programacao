"""
Crie  um  programa  que  auxilie  um  jogador  da  MEGA  SENA  a  criar palpites.  
O  programa  deverá  solicitar  ao  usuário  a  quantidade  de  jogos que serão gerados e, em seguida, sortear aleatoriamente 6 números entre 1 e 60 para cada jogo, armazenando tudo em uma matriz. 
"""
import random

def gerar_palpite():
    palpite = []
    while len(palpite) < 6:
        numero = random.randint(1, 60)
        if numero not in palpite:
            palpite.append(numero)
    palpite.sort()
    return palpite

def gerar_jogos(quantidade_jogos):
    jogos = []
    for _ in range(quantidade_jogos):
        palpite = gerar_palpite()
        jogos.append(palpite)
    return jogos

def main():
    quantidade_jogos = int(input("Quantos jogos você gostaria de gerar? "))    
    jogos = gerar_jogos(quantidade_jogos)    
    print("\nPalpites gerados:")
    for i, jogo in enumerate(jogos, start=1):
        print(f"Jogo {i}: {jogo}")

if __name__ == "__main__":
    main()
