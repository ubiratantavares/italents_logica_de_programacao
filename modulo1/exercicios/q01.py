"""
1.  Receba o  valor de  um produto e calcule o  valor final com  um desconto  de 10%, para isso: 

a.  Escreva  o  algoritmo  em  português  com  detalhes  e  passos  bem definidos. 
b.  Desenhe o fluxograma. 
c.  Escreva  o  pseudocódigo  utilizando  o  portugol. 
d.  Faça  o  teste  de  mesa. 
"""

valor = float(input("Digite o valor do produto: "))
valor_final = valor * (1 - 0.1)
print(valor_final)