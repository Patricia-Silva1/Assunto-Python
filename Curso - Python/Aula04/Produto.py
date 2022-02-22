class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
# preco não pode ter desconto maior que 10%

    def getPreco(self):
        return self.preco
    
    def setPreco(self, valor):
        precoMinimo = self.preco * 0.90
        if (valor < precoMinimo):
            self.preco = precoMinimo
        else:
            self.preco = valor
            
class NovoProduto:
    def __init__(self, nm, pr, ds):
        self.__nome = nm
        self.__preco = pr
        self.__descricao = ds
# preco não pode ter desconto maior que 10%

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        precoMinimo = self.__preco * 0.90
        if (valor < precoMinimo):
            self.__preco = precoMinimo
        else:
            self.__preco = valor