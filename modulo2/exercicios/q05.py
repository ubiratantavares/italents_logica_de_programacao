"""
Escreva um programa que solicite dois números ao usuário e imprima o maior deles ou a mensagem "Números iguais", 
caso sejam iguais.  Para isso,  siga  os  passos  abaixo:

• Solicite ao  usuário  que  informe  o  primeiro  número desejado. 
• Armazene o valor digitado pelo usuário em uma variável, realizando a  conversão  para  float. 
• Solicite ao  usuário  que  informe  o  segundo  número desejado. 
• Armazene o valor digitado pelo usuário em outra variável, realizando a  conversão  para  float. 
• Verifique se os valores das variáveis são iguais. 
• Se  os  valores  forem  iguais,  imprima  a  mensagem  "Números  iguais". 
• Se os valores forem diferentes, verifique qual é o maior deles. 
• Imprima o maior valor encontrado.
"""
from models.numero import Numero

if __name__ == "__main__":
    num1 = Numero()
    num1.ler('Informe  o  primeiro  numero')
    num2 = Numero()
    num2.ler('Informe  o  segundo  numero')    
    num1.comparar(num2)