"""
Faça um programa que utilize uma estrutura de repetição para imprimir a  tabuada  do  8  na  tela.  
O  programa  deve  imprimir  os  resultados  de  1 a 10  para  cada  multiplicação.
"""

from models.tabuada import Tabuada

if __name__ == '__main__':
    tabuada = Tabuada(8)
    tabuada.calcular()