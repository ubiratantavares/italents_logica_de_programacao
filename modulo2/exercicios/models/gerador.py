import random

class Gerador:

    def __init__(self, valor_inicial, valor_final):
        self.__numero = self.escolher_numero_aleatorio(valor_inicial, valor_final)

    @property
    def numero(self):
        return self.__numero

    def escolher_numero_aleatorio(self, valor_inicial, valor_final):
        return random.randint(valor_inicial, valor_final)