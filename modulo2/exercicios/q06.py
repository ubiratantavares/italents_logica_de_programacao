"""
Escreva um programa que solicite ao usuário a nota de um aluno, que deve ser um número real entre 0.0 e 10.0. Em seguida, o programa deve avaliar a nota  do  aluno  de  acordo  com  as  seguintes regras: 

• Se a nota for menor que 6.0, o programa deve imprimir a mensagem "Nota E". 
• Se a nota for de 6.0 até 7.0, o programa deve imprimir a mensagem "Nota D". 
• Se a nota for entre 7.0 e 8.0, o programa deve imprimir a mensagem "Nota  C". 
• Se a nota for entre 8.0 e 9.0, o programa deve imprimir a mensagem "Nota  B". 
• Se a nota for entre 9.0 e 10.0, o programa deve imprimir a mensagem "Nota  A". 

Para isso, siga os passos abaixo: 

• Solicite ao usuário que informe a nota do aluno. 
• Armazene o valor digitado pelo usuário em uma variável, realizando a  conversão  para  float. 
• Verifique  se  a  nota  está  dentro  do  intervalo  permitido  (entre  0.0  e 10.0). 
• Se a nota estiver fora do intervalo, exiba uma mensagem de erro. 
• Se a nota estiver dentro do intervalo, avalie qual a faixa de notas que ela  se  encaixa. 
• Exiba a mensagem correspondente à faixa de notas.
"""

from models.principal import Principal

if __name__ == "__main__":
    programa = Principal()
    programa.executar()