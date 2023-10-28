"""
Reajuste salarial: a empresa iTalents resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará  os  reajustes. 

Faça um programa que solicita o salário atual do colaborador e calcule o reajuste salarial com base nas seguintes faixas salariais: 

• Salários até  R$ 280,00 (incluindo):  aumento de 20%. 
• Salários entre R$ 280,00 e R$ 700,00:  aumento de 15%. 
• Salários entre R$ 700,00 e R$ 1500,00:  aumento de 10%. 
• Salários de R$ 1500,00 em diante:  aumento de 5%. 

Ao final, o programa deverá imprimir na tela as seguintes informações: 

• Salário antes do reajuste. 
• Percentual de aumento aplicado. 
• Valor do aumento. 
• Novo salário após o reajuste. 
"""

from models.funcionario import Funcionario

if __name__ == "__main__":
    funcionario = Funcionario("João", 1980, 12345)
    salario = funcionario.ler_salario("Digite o salário atual do colaborador")
    funcionario.imprimir(salario)
