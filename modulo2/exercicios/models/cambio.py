from models.moeda import Moeda

class Cambio:

    def __init__(self):
        self.__moedas = [Moeda('USD', 5.50), 
                       Moeda('EUR', 6.20), 
                       Moeda('GBP', 7.00), 
                       Moeda('CAD', 4.20), 
                       Moeda('ARS', 0.060), 
                       Moeda('CLP', 0.0070)]
        
    @property
    def moedas(self):
        return self.__moedas

    def obter_cotacao(self, codigo):
        for moeda in self.moedas:
            if moeda.codigo == codigo:
                return moeda.cotacao
        return None

    def converter_para_moeda(self, valor, codigo):
        cotacao = self.obter_cotacao(codigo)
        if cotacao is not None:
            valor_convertido = valor / cotacao
            return f"{codigo} {valor_convertido:.2f}"
        else:
            return "Moeda não suportada"