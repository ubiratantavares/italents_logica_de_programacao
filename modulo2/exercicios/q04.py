"""
Escreva  um  programa  que  solicite  ao  usuário  um  valor  e  verifique  se  o valor é positivo ou negativo. O programa também deve verificar se o valor é diferente de  zero.  Para isso, siga  os  passos  abaixo: 

• Solicite ao usuário que informe o valor desejado. 
• Armazene o valor digitado pelo usuário em uma variável, realizando a  conversão  para  float. 
• Verifique se o valor da variável é maior que 0. 
•   Se o valor for maior que 0, imprima a mensagem "O valor é positivo". 
• Verifique se o valor da variável é menor que 0. 
•   Se o valor for menor que 0, imprima a mensagem "O valor é negativo". 
• Verifique se o valor da variável é igual a 0. 
•   Se  o  valor  for  igual  a  0,  imprima  a  mensagem  "Valor  inválido.  O valor  não  pode  ser  zero."

"""

from models.numero import Numero

if __name__ == "__main__":
    numero = Numero()
    numero.ler("Digite o valor")
    numero.avaliar()