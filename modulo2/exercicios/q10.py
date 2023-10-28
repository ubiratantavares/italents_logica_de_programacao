"""
Jogo  da  adivinhação:  crie um programa que "pense" em um número inteiro  aleatório  entre  0  e  10  e  solicite  ao  usuário  que  tente  adivinhar  o número  escolhido.  O  programa  deve  informar  se  o  usuário  acertou  ou 
errou. 

O  programa  deve  seguir  os  seguintes  passos: 

1) O computador deve escolher um número inteiro aleatório entre 0 e 10. 
2) O  programa  deve  solicitar  que  o  usuário  digite  um número  inteiro entre  0  e  10. 
3) O programa deve comparar o número escolhido pelo usuário com o número  escolhido  pelo  computador. 
4) Se os números forem iguais, o programa deve informar que o usuário venceu. 
5) Se  os  números  forem  diferentes,  o  programa  deve  informar  que  o usuário perdeu e mostrar o número escolhido pelo computador. 
"""

from models.jogo import Jogo

if __name__ == "__main__":
    jogo = Jogo()
    jogo.adivinhar()