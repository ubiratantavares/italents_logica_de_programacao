programa {
  funcao inicio() {
    real valorProduto, desconto, valorFinalProduto
    escreva("Digite o valor do pre�o do produto: ")
    leia(valorProduto)
    desconto = 0.1 * valorProduto
    valorFinalProduto = valorProduto - desconto
    escreva("Valor final do produto: ", valorFinalProduto)
  }
}
