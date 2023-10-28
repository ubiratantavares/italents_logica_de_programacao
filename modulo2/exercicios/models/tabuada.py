class Tabuada:

    def __init__(self, numero):
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero

    def calcular(self):
        for i in range(1, 11):
            resultado = self.numero * i
            print(f'{self.numero} x {i} = {resultado}')