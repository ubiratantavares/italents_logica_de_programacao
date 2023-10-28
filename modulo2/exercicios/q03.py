"""
Escreva um programa que solicite ao usuário um número inteiro e imprima \todos os seus divisores.  

Para isso, siga os passos abaixo: 

• Solicite  ao  usuário  que  informe  o  número  desejado. 
• Armazene o valor digitado pelo usuário em uma variável, realizando a  conversão  para  inteiro. 
• Crie um laço de repetição que percorra todos os números de 1 até o número  digitado  pelo  usuário. 
• Dentro  do  laço  de  repetição,  verifique  se  o  número  digitado  pelo usuário  é  divisível  pelo  número  atual  do  laço,  ou  seja,  se  o  resto da  divisão  é  igual  a  0. 
• Se o resto da divisão for igual a 0, imprima o número atual do laço, pois ele é um divisor do número digitado pelo usuário. 
"""
from models.numero import Numero 

if __name__ == "__main__":
    numero = Numero()
    numero.ler("Digite um numero inteiro: ")
    numero.imprimir_divisores()
