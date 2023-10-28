"""
Crie  um  programa  que  permita ao  usuário inserir  o  nome e a  média  de  um  aluno,  armazenando  também  a  sua  situação  em  um  dicionário.  Ao  final, o  programa  deverá exibir  o conteúdo  da  estrutura  na  tela. A  média  mínima para  aprovação  é  7,  caso  o  aluno  tenha  tirado  entre  5  e  6.9,  ele  estará  em  recuperação, caso  contrário,  ele será  reprovado.
"""

from models.aluno import Aluno

if __name__ == '__main__':
    alunos = {}
    id = 1
    while True:
        nome = input("Digite o nome do aluno (ou 'q' para sair): ")
        if nome == 'q':
            break
        media = float(input("Digite a média do aluno: "))        
        aluno = Aluno(nome, media)
        alunos[id] = aluno
        id += 1
    print("\nConteúdo do dicionário:")
    for nome, aluno in alunos.items():
        print(f"Nome: {aluno.nome}, Média: {aluno.media}, Situação: {aluno.situacao}")
