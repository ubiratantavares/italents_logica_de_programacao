"""
Desenvolva  um  programa  que  crie  uma  matriz  com  informações  de  5 clientes,  sendo  5  nomes  e  5  idades.  Utilizando  as  estruturas  de  repetição "for"  e  "if",  verifique  quais  clientes  são  maiores  de  idade  e  quais  são menores  de  idade,  exibindo  na  tela  a  seguinte  frase  para  cada  um  deles:  

"fulano é maior de idade" ou "fulana é menor de idade". O programa deve informar  ainda  a  quantidade  de  clientes  maiores  e  menores  de  idade. 
"""

from models.pessoa import Cliente
from models.cliente import Clientela

if __name__ == '__main__':
    
    c = Clientela()
    c.adicionar(Cliente("Paulo", 25))
    c.adicionar(Cliente("Maria", 17))
    c.adicionar(Cliente("Joao", 30))
    c.adicionar(Cliente("Ana", 16))
    c.adicionar(Cliente("Pedro", 22))

    c.imprimir()