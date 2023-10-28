"""
1.  Conversor de moedas: crie um programa que solicite ao usuário um valor em reais (R$) e converta esse valor para outras moedas, tais como: 

• Dólar Americano (USD) 
• Euro  (EUR) 
• Libra  Esterlina  (GBP) 
• Dólar  Canadense  (CAD) 
• Peso Argentino (ARS) 
• Peso  Chileno  (CLP) 

Para  realizar  as  conversões,  você  precisará  realizar  uma  pesquisa  para 
saber  a  cotação  de  cada  moeda  em  real. 

O resultado da conversão deve ser exibido no formato:

U$9999.99 (para dólar americano), 
€9999.99 (para euro), 
£9999.99 (para libra esterlina), 
C$9999.99 (para  dólar  canadense),  
ARS  9999.99  (para  peso  argentino),
CLP  9999.99  (para  peso  chileno).
"""
from models.cambio import Cambio

def main():
    cambio = Cambio()    
    valor_em_reais = float(input("Digite o valor em reais (R$): "))    
    print("Escolha a moeda para a conversão:")
    for i, moeda in enumerate(cambio.moedas, start=1):
        print(f"{i} - {moeda.codigo} ({moeda.codigo})")
    opcao = int(input("Digite o número da moeda desejada: "))
    if 1 <= opcao <= len(cambio.moedas):
        moeda = cambio.moedas[opcao - 1].codigo
        resultado = cambio.converter_para_moeda(valor_em_reais, moeda)
        if resultado != "Moeda não suportada":
            print(f"Valor convertido: {resultado}")
    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()