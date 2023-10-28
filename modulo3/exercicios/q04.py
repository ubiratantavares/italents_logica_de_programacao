"""
Desenvolva  um  programa  que  permita  ao  usuário  inserir  diversos  números em  uma  lista.  Em  seguida,  o  programa  deverá  criar  duas  listas  extras que armazenem  somente  os  valores  pares  e  os  valores  ímpares  digitados,  
respectivamente. Ao final, o programa deve exibir o conteúdo das três listas geradas. 
"""
def ler_numeros():
    numeros = []
    while True:
        try:
            numero = int(input("Digite um número (ou qualquer letra para encerrar): "))
            numeros.append(numero)
        except ValueError:
            break
    return numeros

def separar_pares_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def main():
    numeros = ler_numeros()
    pares, impares = separar_pares_impares(numeros)
    print("Todos os números digitados: ", numeros)
    print("Números pares: ", pares)
    print("Números ímpares: ", impares)

if __name__ == "__main__":
    main()
