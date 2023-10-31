"""
Receba  três  números  do  usuário  e  os  exiba em  ordem  crescente, para isso: 

a.  Escreva  o  algoritmo  em  português  com  detalhes  e  passos  bem 
definidos. 
b.  Desenhe o fluxograma. 
c.  Escreva  o  pseudocódigo  utilizando  o  portugol. 
d.  Faça  o  teste  de  mesa. 
"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 <= num2 <= num3:
    print(f"{num1}, {num2}, {num3}")
if num1 <= num3 <= num2:
    print(f"{num1}, {num3}, {num2}")
if num2 <= num1 <= num3:
    print(f"{num2}, {num1}, {num3}")
if num2 <= num3 <= num1:
    print(f"{num2}, {num3}, {num1}")
if num3 <= num1 <= num2:
    print(f"{num3}, {num1}, {num2}")
if num3 <= num2 <= num1:
    print(f"{num3}, {num2}, {num1}")