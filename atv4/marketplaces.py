class Marketplace:
    marketplace = [
        'B2W',
        'Amazon',
        'Mercado Livre'
    ]

class Category:
    categories = {
        'Mobile': ['Celulares', 'Tablets'],
        'Móveis': ['Mesa', 'Guarda-Roupa'],
        'Eletrônicos': ['TV', 'Rádio']
    }

def categorias():
    print('Categorias')

    for c in Category:
        print(c)