import random

class Jogador:
    
    def __init__(self, nome):
        self.nome = nome
        self.resultados = []
        self.vitorias = 0

    def jogar_dado(self):
        resultado = random.randint(1, 6)
        self.resultados.append(resultado)
        return resultado