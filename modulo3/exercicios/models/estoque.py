class Estoque:
    
    def __init__(self):
        self.__produtos = []

    @property
    def produtos(self):
        return self.__produtos

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.validar_produto(codigo):
                return produto
        return None
    
    def exibir_produtos(self):
        for produto in self.produtos:
            print(produto)