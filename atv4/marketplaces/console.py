from marketplaces import Marketplace, Category, Subcategory, Data

marketplaces = []
result_marketplaces = Data.get_marketplaces()
for i in result_marketplaces:
    marketplaces.append(Marketplace(i['marketplaces']))

categories = []
result_categories = Data.get_categories()
for i in result_categories:
    for j in marketplaces:
        if i['marketplaces'] == j.get_name():
            categories.append(Category(i['categories'], j))

subcategories = []
result_subcat = Data.get_subcat()
for i in result_subcat:
    for j in categories:
        if i['categories'] == j.get_name():
            subcategories.append(Subcategory(i['subcategories'], j))
            break

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
            for i in categories:
                if i.get_parentname() ==  marketplaces[0].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nDigite uma opção de categoria: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategories:
                            if i.get_parentname() == categories[1].get_name():
                                print(f'\n Menu de categories:')
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break
                
        elif op == 2:
            item = 1
            print(f'\nVocê escolheu a opção {marketplaces[1]}\n')
            for i in categories:
                if i.get_parentname() ==  marketplaces[1].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nDigite uma opção de categoria: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategories:
                            if i.get_parentname() == categories[0].get_name():
                                print(f'\n{i.get_subcat()}')

                        break
                except Exception as e: 
                    print(e)
                
        elif op == 3:
            item = 1
            print(f'\nVocê escolheu a opção {marketplaces[2]}\n')
            for i in categories:
                if i.get_parentname() ==  marketplaces[2].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nDigite uma opção de categoria: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategories:
                            if i.get_parentname() == categories[0].get_name():
                                print(f'\n{i.get_subcat()}')
                        break
                except Exception as e: 
                    print(e)
                    break

        elif op == 4:
            item = 1
            print(f'\nVocê escolheu a opção {marketplaces[3]}\n')
            for i in categories:
                if i.get_parentname() ==  marketplaces[3].get_name():
                    print(f'{item} - {i.get_name()}')
                    item += 1
            escolher_cat = int(input(f'\nDigite uma opção de categoria: '))
            while True:
                try:
                    if escolher_cat == 1:
                        for i in subcategories:
                            if i.get_parentname() == categories[0].get_name():
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