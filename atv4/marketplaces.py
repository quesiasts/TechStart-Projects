class Marketplaces:
    marketplaces = [
                            'AM': 'Amazon',
                            'B2W': 'B2W',
                            'ML': 'Mercado Livre',
                            'MG': 'Magalu'
                            ]

class Category:
    categories = [
                'MOVEIS': 'Móveis',
                'ELETRÔNICOS': 'Eletrônicos',
                'MOBILE': 'Mobile'
                ]

class Subcategory(Category):
    subcategories = [
                    'MESA': 'Mesa',
                    'ESCRIVANINHA': 'Escrivaninha',
                    'TV': 'TV',
                    'COMPUTADORES': 'Computadores',
                    'CELULARES': 'Celulares',
                    'TABLET': 'Tablet'
                    ]