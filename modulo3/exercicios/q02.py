"""
Desenvolva  um  programa  que  faça  5  perguntas  para  o  usuário  referentes 
a  um  crime.  

As  perguntas  são: 

• "Você telefonou para a vítima?"
• "Esteve  no  local  do crime?"
• "Mora perto da vítima?"
• "Devia para a vítima?"
• "Já trabalhou com a vítima?"

Ao  final  das  perguntas,  o  programa  deverá  emitir  uma  classificação  sobre a  possível  participação  do  usuário  no  crime.  

Caso  o  usuário  tenha respondido  positivamente  a  duas  perguntas,  deverá  ser  classificado  como "suspeito"; 

entre 3 e 4 respostas positivas, como "cúmplice"; 

5 respostas positivas,  como  "assassino",  

caso  contrário,  será  classificado  como "inocente". 
"""

def perguntar(mensagem):
    return input(f"\n{mensagem}\n[S/N]: ").upper() == "S"

def emitir(contador):
    if contador == 2:
        print("\nsuspeito\n")
    elif (contador >= 3) and (contador <= 4):
        print("\ncúmplice\n")
    elif (contador == 5):
        print("\nassassino\n")
    else:
        print("\ninocente\n")

if __name__ == "__main__":
    contador = 0    
    if perguntar("Você telefonou para a vítima? "):
        contador += 1    
    if perguntar("Esteve  no  local  do crime? "):
        contador += 1
    if perguntar("Mora perto da vítima? "):
        contador += 1
    if perguntar("Devia para a vítima? "):
        contador += 1
    if perguntar("Já trabalhou com a vítima? "):
        contador += 1
    emitir(contador)
