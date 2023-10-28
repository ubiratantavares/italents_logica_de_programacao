class Aluno:

    def __init__(self):
        self.nota = 0

    def ler_nota(self, mensagem):
        self.nota = float(input(f'{mensagem}: '))

    def validar_nota(self):
        if self.nota < 0 or self.nota > 10:
            return False
        return True

    def avaliar_nota(self):
        if self.nota < 6.0:
            return "Nota E"
        elif self.nota < 7.0:
            return "Nota D"
        elif self.nota < 8.0:
            return "Nota C"
        elif self.nota < 9.0:
            return "Nota B"
        return "Nota A"
    