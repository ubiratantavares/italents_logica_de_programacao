class Cliente:
    
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade

    def verificar_maior_idade(self):
        if self.idade >= 18:
            return True
        return False        

    def __str__(self):
        if self.verificar_maior_idade():
            return f"{self.nome} é maior de idade."
        return f"{self.nome} é menor de idade."