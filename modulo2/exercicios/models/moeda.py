class Moeda:

    def __init__(self, codigo, cotacao):
        self.__codigo = codigo
        self.__cotacao = cotacao

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def cotacao(self):
        return  self.__cotacao
    
    def __str__(self):
        return f'Moeda {self.codigo} com cotação de R$ {self.cotacao}'