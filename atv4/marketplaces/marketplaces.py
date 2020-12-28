class Marketplace:
    def __init__(self, Marketplace: str):
        self.__namemkp = Marketplace

    def get_name(self) -> str:
        return self.__namemkp

    def __str__(self) -> str:
        return f'''{self.__namemkp}'''

class Category:
    def __init__(self, Category: str, Marketplace: Marketplace):
        self.__catmkp = Category
        self.__parent = Marketplace

    def get_name(self) -> str:
        return self.__catmkp

    def get_parentname(self) -> str:
        return self.__parent.get_name()

class Subcategory:
    def __init__(self, Subcategory: str, Category: Category):
        self.__subcat = Subcategory
        self.__parent = Category

    def get_subcat(self) -> str:
        return self.__subcat

    def get_parentname(self) -> str:
        return self.__parent.get_name

class Dados:
    def get_marketplaces():
        marketplaces = []
        archive = open('marketplaces.txt', 'r') #r -> ler arquivo de texto
        for i in archive:
            i = i.strip() #strip -> tirar o \n
            i = {'marketplace':i}
            marketplaces.append(i) #append -> adiciona sempre a ultima posição
        archive.close()
        return marketplaces

    def get_categories():
        categorias = []
        archive = open('dados/categorias.txt', 'r') 
        for i in archive:
            i = i.strip()
            j = i.split(';') # split -> separar atributos com ponto e vírgula
            i = {'categories': j[1],
                'marketplaces': j[0]
            }
            categorias.append(i)
        archive.close()
        return categorias

    def get_subcategories():
        subcategorias = []
        archive = open('dados/subcategorias.txt', 'r') 
        for i in archive:
            i = i.strip()
            j = i.split(';')
            i = {'subcategorias': j[1],
                'categories': j[0]
            }
            subcategories.append(i)
        archive.close()
        return subcategorias