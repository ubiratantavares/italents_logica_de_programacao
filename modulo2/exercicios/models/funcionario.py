class Funcionario:

    def __init__(self, nome, ano_nascimento, ctps):
        self.__nome = nome
        self.__ano_nascimento = ano_nascimento
        self.__ctps = ctps
        self.__ano_contratacao = None
        self.__salario = None

    @property
    def salario(self):
        return self.__nome
    
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

    def ler_salario(self, mensagem):
        self.salario = float(input(f'{mensagem}: '))

    def aplicar_percentual(self):
        limites_percentuais = [(280, 20), (700, 15), (1500, 10)]
        for limite, percentual in limites_percentuais:
            if self.salario <= limite:
                return percentual
        return 5

    def atualizar_salario(self):
        return self.salario * (1 + self.aplicar_percentual() / 100)

    def imprimir(self):
        print('Salário antes do reajuste:', f'R$ {self.salario}')
        print('Percentual de aumento aplicado: ', f'{self.aplicar_percentual()} %')
        print('Valor do aumento: ', f'R$ {self.atualizar_salario() - self.salario}')
        print('Novo salário: ', f'R$ {self.atualizar_salario()}')