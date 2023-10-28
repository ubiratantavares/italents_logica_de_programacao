class Clientela:

    def __init__(self):
        self.__clientes = []

    @property
    def clientes(self):
        return self.__clientes

    def adicionar(self, cliente):
        self.clientes.append(cliente)

    def contar(self):
        maior_idade = 0
        menor_idade = 0
        for cliente in self.clientes:
            if cliente.idade >= 18:
                maior_idade += 1
            else:
                menor_idade += 1
        return maior_idade, menor_idade

    def imprimir(self):
        for cliente in self.clientes:
            print(cliente)
        maior_idade, menor_idade = self.contar()
        print(f"Total de clientes maiores de idade: {maior_idade}")
        print(f"Total de clientes menores de idade: {menor_idade}")