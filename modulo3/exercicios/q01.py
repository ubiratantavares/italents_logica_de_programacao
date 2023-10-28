"""
Crie  um  programa  que  utilize  a lista  L  = [5,  7,  2,  9,  4,  1, 3]  e exiba  as 
seguintes informações: 

• Quantidade de elementos presentes na lista. 
• O maior valor presente na lista. 
• O menor valor presente na lista. 
• A  soma  de  todos  os  elementos  da  lista. 
• A  lista  em  ordem  crescente. 
• A  lista  em  ordem  decrescente. 
"""

def quantidade_elementos(lista):
    return len(lista)

def maior_elemento(lista):
    return max(lista)

def menor_elemento(lista):
    return min(lista)

def soma_elementos(lista):
    return sum(lista)

def lista_ordenada_crescente(lista):
    return sorted(lista)

def lista_ordenada_descrecente(lista):
    return sorted(lista, reverse=True)

if __name__ == "__main__":
    
    lista  = [5,  7,  2,  9,  4,  1, 3]

    print(f"Quantidade de Elementos: {quantidade_elementos(lista)}")

    print(f"O maior valor presente na lista: {maior_elemento(lista)}")

    print(f"O menor valor presente na lista: {menor_elemento(lista)}")

    print(f"A soma dos elementos: {soma_elementos(lista)}")

    print(f"Lista em ordem crescente: {lista_ordenada_crescente(lista)}")

    print(f"Lista em ordem decrescente: {lista_ordenada_descrecente(lista)}")
