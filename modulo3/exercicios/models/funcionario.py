import datetime

class Funcionario:

    def __init__(self, nome, ano_nascimento, ctps):
        self.__nome = nome
        self.__ano_nascimento = ano_nascimento
        self.__ctps = ctps
        self.__ano_contratacao = None
        self.__salario = None

    @property
    def nome(self):
        return self.__nome.title()
    
    @property
    def ano_nascimento(self):
        return self.__ano_nascimento
    
    @property
    def ctps(self):
        return self.__ctps
    
    @property
    def ano_contratacao(self):
        return self.__ano_contratacao
    
    @property
    def salario(self):
        return self.__salario

    def calcular_idade(self):
        return datetime.datetime.now().year - self.ano_nascimento

    def calcular_aposentadoria(self):
        idade = self.calcular_idade()
        ano_atual = datetime.datetime.now().year
        if self.ctps != 0:
            anos_contribuicao = ano_atual - self.ano_contratacao
            anos_restantes = 35 - anos_contribuicao
            ano_aposentadoria = ano_atual + anos_restantes
            return ano_aposentadoria
        else:
            return None

    def preencher_dados_profissionais(self, ano_contratacao, salario):
        self.__ano_contratacao = ano_contratacao
        self.__salario = salario

    def exibir_informacoes(self):
        print("*** Informações do Funcionário ***")
        print(f"Nome: {self.nome}")
        print(f"Ano de Nascimento: {self.ano_nascimento}")
        print(f"Número da Carteira de Trabalho (CTPS): {self.ctps}")

        if self.ctps != 0:
            print(f"Ano de Contratação: {self.ano_contratacao}")
            print(f"Salário: R$ {self.salario:.2f}")
            idade = self.calcular_idade()
            print(f"Idade: {idade} anos")
            ano_aposentadoria = self.calcular_aposentadoria()
            if ano_aposentadoria:
                print(f"Ano de Aposentadoria: {ano_aposentadoria}")
            else:
                print("O funcionário não tem informações de CTPS para calcular a aposentadoria.")
