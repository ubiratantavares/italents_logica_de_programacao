class Aluno:

    def __init__(self, nome, media):
        self.__nome = nome
        self.__media = media
        self.__situacao = self.avaliar_situacao()

    @property
    def nome(self):
        return self.__nome
    
    @property
    def media(self):
        return self.__media
    
    @property
    def situacao(self):
        return self.__situacao

    def avaliar_situacao(self):
        if self.media >= 7:
            return "Aprovado"
        elif 5 <= self.media < 7:
            return "Recuperação"
        else:
            return "Reprovado"