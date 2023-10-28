class Numero:

    def __init__(self):
        self.__valor = 0

    @property
    def valor(self):
        return self.__valor

    def ler(self, mensagem):
        self.__valor = int(input(f'{mensagem}: '))

    def eh_par(self):
        if self.valor % 2 == 0:
            return True
        return False

    def imprimir_paridade(self):
        if self.eh_par():
            print("O número é par")
        else:
            print("O número é ímpar")

    def imprimir_divisores(self):
        for i in range(1, self.valor + 1):
            if (self.valor % i == 0):
                print(i)

    def avaliar(self):
        if self.valor < 0:
            print("O valor é negativo")
        elif self.valor > 0:
            print("O valor é positivo")
        else:
            print('Valor inválido. O valor não pode ser zero')

    def comparar(self, numero):
        if (self.valor == numero.valor):
            print("Numeros iguais")
        elif (self.valor > numero.valor):
            print(f"O maior numero eh {self.valor}")
        else:
            print(f"O maior numero eh {numero.valor}")