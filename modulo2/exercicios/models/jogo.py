import random

from models.gerador import Gerador

class Jogo:

    def __init__(self):
        self.__numero = None

    @property
    def numero(self):
        return self.__numero

    def adivinhar(self):
        while True:
            try:
                self.__numero = Gerador(0, 10)
                palpite = int(input("Tente adivinhar o número entre 0 e 10: "))
                if 0 <= palpite <= 10:
                    if palpite == self.numero:
                        print("Parabéns! Você acertou o número!")
                        break
                    else:
                        print(f"Você errou. O número escolhido pelo computador era {self.numero}. Tente novamente.")
                else:
                    print("Por favor, digite um número entre 0 e 10.")
            except ValueError:
                print("Por favor, digite um número válido.")
                