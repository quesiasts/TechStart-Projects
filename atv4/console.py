from marketplaces import Marketplaces, Category, SubCategory

def marketplace():


def category():

def menu():
    options = ["Cadastrar Marketplace", "Cadastrar Categorias"]

    print("\nMenu:")
    for i, option in enumerate(options):
        print(f"[{i+1}] - {option}")

        op = int(input("Choose an option: "))
        return op

while True:
    try:
        op == menu()
        if op == 1:
            marketplace()
        elif op == 2:
            category()
        elif op == 3:
            exit(0)
        else:
            print("Opção indisponível")
    except ValueError:
        print("Opção indisponível")