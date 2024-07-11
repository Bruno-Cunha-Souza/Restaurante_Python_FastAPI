from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de laranja', 7.50 , 'grande')
prato_pao  = Prato('Pão na chapa', 6.50, 'Pão frances na chapa com manteiga')

def main():
    print(bebida_suco)

if __name__ == '__main__':
    main()