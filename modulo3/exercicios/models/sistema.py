from models.produto import Produto
from models.estoque import Estoque
from models.cliente import Cliente

class Sistema:

    def __init__(self):
        self.__estoque = self.abastecer_estoque()
        self.__cliente = Cliente("João")

    @property
    def estoque(self):
        return self.__estoque
    
    @property
    def cliente(self):
        return self.__cliente

    def abastecer_estoque(self):
        produto1 = Produto(1, "Arroz", 5.0, 50)
        produto2 = Produto(2, "Feijão", 4.0, 40)
        produto3 = Produto(3, "Macarrão", 2.0, 40)
        estoque = Estoque()
        estoque.adicionar_produto(produto1)
        estoque.adicionar_produto(produto2)
        estoque.adicionar_produto(produto3)
        return estoque

    def obter_codigo_produto(self):
        return int(input("\nDigite o código do produto (0 para finalizar): "))

    def processar_produto(self, produto):
        if produto:
            quantidade = int(input(f"Digite a quantidade de {produto.nome} desejada: "))
            if produto.validar_estoque(quantidade):
                self.cliente.adicionar_produto(produto, quantidade)
                produto.atualizar_estoque(quantidade)
            else:
                print(f"\nQuantidade indisponível em estoque para {produto.nome}")
        else:
            print("\nProduto não encontrado")

    def executar(self):
        while True:
            codigo = self.obter_codigo_produto()
            if codigo == 0:
                break
            produto = self.estoque.buscar_produto(codigo)
            self.processar_produto(produto)
        self.cliente.exibir_compras()
        self.estoque.exibir_produtos()