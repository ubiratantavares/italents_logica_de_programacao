"""
Crie  um  programa  que  permita  ao  usuário  inserir  diversos  valores numéricos  em  uma  lista.  Caso  o  valor  já  tenha  sido  digitado anteriormente,  ele  não  será  adicionado  novamente.  Ao  final,  o  programa deve exibir todos os valores  únicos  digitados  em  ordem  crescente.
"""

def inserir_valores_unicos():
    lista = []
    while True:
        valor = input("Digite um valor numérico (ou digite 'sair' para encerrar): ")        
        if valor.lower() == 'sair':
            break        
        try:
            valor = float(valor)
        except ValueError:
            print("Valor inválido. Por favor, digite um valor numérico.")
            continue        
        if valor not in lista:
            lista.append(valor)
    return lista

def exibir_valores_unicos_ordenados(lista):
    lista.sort()
    print("Valores únicos em ordem crescente:")
    for valor in lista:
        print(valor)

if __name__ == "__main__":
    lista = inserir_valores_unicos()
    exibir_valores_unicos_ordenados(lista)
