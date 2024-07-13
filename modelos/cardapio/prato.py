from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
    
    def __str__(self):
        return self._nome
    
    def aplic_descont(self):
        self._preco -= (self._preco * 0.06)