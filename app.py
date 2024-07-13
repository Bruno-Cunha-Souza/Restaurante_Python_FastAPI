from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de laranja', 7.50 , 'grande')
bebida_suco.aplic_descont()
prato_pao  = Prato('Pão na chapa', 6.50, 'Pão frances na chapa com manteiga')
prato_pao.aplic_descont()
restaurante_praca.add_item_cardapio(bebida_suco)
restaurante_praca.add_item_cardapio(prato_pao)

def main():
    restaurante_praca.show_cardapio

if __name__ == '__main__':
    main()