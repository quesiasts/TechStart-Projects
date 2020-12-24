from marketplaces import Marketplace, Category, Subcategory

marketplaces = [Marketplace('Amazon'), Marketplace('B2W'), Marketplace('Mercado Livre'), Marketplace('Via Varejo'), Marketplace('Sair')]
categorias = [Category('Móveis', marketplaces[1]), Category('Telefonia', marketplaces[0]), Category('Eletrodomésticos', marketplaces[1]), Category('Informática', marketplaces[1])]
subcategorias = [Subcategory('Cama', categorias[0]), Subcategory('Cadeira', categorias[0]), Subcategory('Mesa', categorias[1])]

def menu(): 

    print('\nMENU: ')

    i = 1
    for option in marketplaces:
        print(f'{i} - {option}')
        i += 1

    op = int(input('Selecione uma opção: '))
    return op

while True:
    try:
        op = menu()
        if op == 1:
            item = 1
            print(f'\nVocê escolheu a opção {marketplaces[0]}\n')
            for i in categorias:
                if i.get_parentname() ==  marketplaces[0].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nDigite uma opção de categoria: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategorias:
                            if i.get_parentname() == categorias[1].get_name():
                                print(f'\n Menu de categorias:')
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break
                
        elif op == 2:
            item = 1
            print(f'\nVocê escolheu a opção {marketplaces[1]}\n')
            for i in categorias:
                if i.get_parentname() ==  marketplaces[1].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nDigite uma opção de categoria: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategorias:
                            if i.get_parentname() == categorias[0].get_name():
                                print(f'\n{i.get_subcat()}')

                        break
                except Exception as e: 
                    print(e)
                
        elif op == 3:
            item = 1
            print(f'\nVocê escolheu a opção {marketplaces[2]}\n')
            for i in categorias:
                if i.get_parentname() ==  marketplaces[2].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nDigite uma opção de categoria: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategorias:
                            if i.get_parentname() == categorias[0].get_name():
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break

        elif op == 4:
            item = 1
            print(f'\nVocê escolheu a opção {marketplaces[3]}\n')
            for i in categorias:
                if i.get_parentname() ==  marketplaces[3].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nDigite uma opção de categoria: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategorias:
                            if i.get_parentname() == categorias[0].get_name():
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break
            
        elif op == 5:
            exit(0) #tentar alterar
        else:
            print('Digite uma opção válida!')
        break

    except ValueError:
        print('Opção indisponível. Tente novamente.')