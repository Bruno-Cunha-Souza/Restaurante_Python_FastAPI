from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self,  nome, preco) :
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplic_descont(self):
        pass