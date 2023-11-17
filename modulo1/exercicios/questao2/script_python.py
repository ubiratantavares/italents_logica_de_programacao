"""
2.  Solicite ao usuário que insira uma temperatura em graus Celsius e converta-a para Fahrenheit, para isso: 

a.  Escreva  o  algoritmo  em  português  com  detalhes  e  passos  bem definidos. 
b.  Desenhe o fluxograma. 
c.  Escreva  o  pseudocódigo  utilizando  o  portugol. 
d.  Faça  o  teste  de  mesa. 
"""

tempCelsius = float(input("Digite a temperatura em graus Celsius: "))
tempFahrenheit = 9 / 5 * tempCelsius + 32
print("A temperatura em graus Fahrenheit: ", tempFahrenheit)