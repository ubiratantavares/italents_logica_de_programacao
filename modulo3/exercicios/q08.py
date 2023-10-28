"""
Elabore  um  programa  que  utilize  um  dicionário  para  simular  a  baixa  de  estoque  das  vendas  de  um  supermercado.  O  programa  deve  realizar  as seguintes  validações: 

• Verificar  se  o  produto está  disponível  no  estoque. 
• Validar se  o  produto informado  é  válido. 
• Verificar  se  a  quantidade  solicitada  está  disponível  no  estoque. 

Ao  final,  o  programa  deve  exibir  para  o  cliente  a  quantidade  de  itens comprados e  o  valor total  da compra. 
"""
from models.sistema import Sistema

if __name__ == "__main__":
    sistema = Sistema()
    sistema.executar()
