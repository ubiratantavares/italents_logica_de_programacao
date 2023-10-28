"""
Agora, imprima todas as tabuadas do número 1 ao 10.
"""
from models.tabuada import Tabuada

if __name__ == '__main__':

    for valor in range(1, 11):
        tabuada = Tabuada(valor)
        tabuada.calcular()