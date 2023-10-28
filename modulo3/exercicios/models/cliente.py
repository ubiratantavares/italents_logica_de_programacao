class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome
        self.__carrinho = []

    @property
    def nome(self):
        return  self.__nome
    
    @property
    def carrinho(self):
        return self.__carrinho

    def adicionar_produto(self, produto, quantidade):
        self.carrinho.append((produto, quantidade))

    def exibir_compras(self):
        total_compra = 0
        total_itens = 0
        print(f"\nCarrinho de compra do cliente {self.nome}:")
        for item in self.carrinho:
            produto, quantidade = item
            valor_item = produto.calcular_valor_total(quantidade)
            print(f"{produto.nome}: {quantidade} x {produto.preco} = R$ {valor_item:.2f}")
            total_compra += valor_item
            total_itens += 1
        print(f"\nTotal de itens comprados: {total_itens}")
        print(f"Total da compra: R$ {total_compra:.2f}\n")