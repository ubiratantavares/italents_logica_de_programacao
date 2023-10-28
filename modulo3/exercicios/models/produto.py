class Produto:
    
    def __init__(self, codigo, nome, preco, quantidade):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco # preco unitário
        self.__quantidade = quantidade # quantidade em estoque

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def quantidade(self):
        return self.__quantidade

    def validar_produto(self, codigo):
        return codigo == self.codigo

    def validar_estoque(self, quantidade):
        return quantidade <= self.quantidade

    def atualizar_estoque(self, quantidade):
        self.__quantidade -= quantidade

    def calcular_valor_total(self, quantidade):
        return quantidade * self.preco
    
    def __str__(self):
        return f'Codigo: {self.codigo}, Nome: {self.nome}, Preco: R$ {self.preco}, Quantidade: {self.quantidade}'