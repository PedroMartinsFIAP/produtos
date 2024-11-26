class Produto:
    produtos = []

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        Produto.produtos.append(self)

    def __str__(self):
        return f'{self.nome} | {self.preco}'
    
    def exibir_produto():
        for produto in Produto.produtos:
            print (f'Produto: {produto.nome} | Preço: R${produto.preco}') 

notebook = Produto ('Notebook', '4.719,90')
celular = Produto ('Smartphone', '1918,93')
fone = Produto ('Fone de ouvido', '189,87')


Produto.exibir_produto()
