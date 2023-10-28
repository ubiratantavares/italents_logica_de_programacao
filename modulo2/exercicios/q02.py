"""
Escreva um programa que solicite ao usuário um número e verifique se esse número é par ou ímpar.  

Para isso, siga os passos abaixo: 

• Solicite  ao  usuário  que  informe  o  número  desejado. 
• Armazene o valor digitado pelo usuário em uma variável, realizando a  conversão  para  inteiro. 
• Verifique se o valor da variável é divisível por 2,  ou seja, se o resto da  divisão  por  2  é  igual  a  0. 
• Se  o  resto  da  divisão por  2  for  igual  a  0 , imprima  a  mensagem  "O número  é  par". 
• Caso contrário, ou seja, se o resto da divisão por 2 for diferente de 0, imprima a  mensagem  "O  número  é ímpar".

"""
from models.numero import Numero

if __name__ == "__main__":
    numero = Numero()
    numero.ler("Informe o número desejado: ")
    numero.imprimir_paridade()