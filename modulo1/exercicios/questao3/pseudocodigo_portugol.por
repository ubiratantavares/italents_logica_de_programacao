programa {
  funcao inicio() {
    real num1, num2, num3, aux

    escreva("Digite o primeiro valor: ")
    leia(num1)
    escreva("Digite o segundo valor: ")
    leia(num2)
    escreva("Digite o terceiro valor: ")
    leia(num3)
       // Verificar e ordenar os valores em ordem crescente
    se (num1 > num2) {
      aux = num2
      num2 = num1
      num1 = aux
    }
    se (num2 > num3) {
      aux = num3
      num3 = num2
      num2 = aux
    }
    se (num1 > num2) {
      aux = num2
      num2 = num1
      num1 = aux
    }
    escreva("Valores em ordem crescente: ", num1, ", ", num2, ", ", num3)
  }
}
