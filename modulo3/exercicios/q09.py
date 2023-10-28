"""
Desenvolva  um  programa  que  solicite  ao  usuário  o  nome,  ano  de nascimento  e  número  da  carteira  de  trabalho  (CTPS),  armazenando  essas informações  em  um  dicionário. 
Caso  a  CTPS  informada  seja  diferente  de zero,  o  programa  deve  solicitar  o  ano  de  contratação  e  o  salário  do funcionário. 
Com  base  nas  informações  coletadas,  o  programa  deve  calcular  e acrescentar,  no  dicionário,  a  idade  do  funcionário  e  com  quantos  anos  ele irá  se  aposentar.  Considere  que  o  trabalhador  deve  contribuir  por  35  anos para se  aposentar. 
Ao  final,  o  programa  deve  exibir  o  conteúdo  completo  do  dicionário, 
incluindo  os  dados  pessoais,  profissionais  e  o cálculo  da  aposentadoria. 
"""
from models.funcionario import Funcionario

if __name__ == "__main__":
    funcionario = Funcionario("João", 1980, 12345)
    if funcionario.ctps != 0:
        funcionario.preencher_dados_profissionais(2005, 5_000)
    funcionario.exibir_informacoes()