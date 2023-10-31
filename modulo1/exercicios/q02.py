"""
2.  Solicite ao usuário que insira uma temperatura em graus Celsius e converta-a para Fahrenheit, para isso: 

a.  Escreva  o  algoritmo  em  português  com  detalhes  e  passos  bem definidos. 
b.  Desenhe o fluxograma. 
c.  Escreva  o  pseudocódigo  utilizando  o  portugol. 
d.  Faça  o  teste  de  mesa. 

9 * Tc = 5 * (Tf - 32)
9 * Tc = 5 * Tf - 160



"""

def converter_temperatura(temp_celsius):
    return 9 / 5 * temp_celsius + 32

print(converter_temperatura(0))
print(converter_temperatura(100))