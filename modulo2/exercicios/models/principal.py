from models.aluno import Aluno

class Principal:

    def __init__(self):
        self.aluno = Aluno()

    def executar(self):
        self.aluno.ler_nota("Digite a nota")
        while not self.aluno.validar_nota():
            print('Nota inválida!')
            self.aluno.ler_nota("Digite a nota")
        resultado = self.aluno.avaliar_nota()
        print(resultado)