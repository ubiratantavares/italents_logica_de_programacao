programa {
  funcao inicio() {
    real valorProduto, desconto, valorFinalProduto
    escreva("Digite o valor do preço do produto: ")
    leia(valorProduto)
    desconto = 0.1 * valorProduto
    valorFinalProduto = valorProduto - desconto
    escreva("Valor final do produto: ", valorFinalProduto)
  }
}
