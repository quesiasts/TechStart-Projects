class Produtos:
    produtos = []

    def set_produto(self):
        nome = input('Coloque o nome do Produto: ')
        descricao = input('Coloque uma descrição para o produto: ')
        dimensao = input('Adicione a dimensão do produto:')
        categoria = input('Adicione um categoria: ')
        preco = input('Adicione o valor: ')
        self.produtos.append({
            'nome': nome,
            'descrição': descricao[1:20],
            'dimensão': dimensao,
            'categoria': categoria,
            'preco': preco 
        })

    def listar_produtos(self):
        for produto in self.produtos:
            nome, descricao, dimensao, categoria, preco = produto.values()
            print('Nome: ' + nome + 
            ' Descrição: ' + descricao +
            ' Dimensão: ' + dimensao +
            ' Categoria: ' + categoria + 
            ' Preço: ' + str(preco))
produto = Produtos()

class Categorias:
    categorias = []

    def cadastrar_categoria(self):
        nomeCategoria = input('Coloque um nome para a categoria: ')
        self.categorias.append({
            'nomeCategoria': nomeCategoria
        })

    def listar_categoria(self):
        for categoria in self.categorias:
            nomeCategoria = categoria.values()
            print(' Categoria: ' + str(nomeCategoria))
categoria = Categorias()

class SubCategorias:
    subCat = []

    def cadastrar_subCategoria(self):
        nomeSubCategoria = input('Coloque um nome para a Subcategoria: ')
        self.subCat.append({
            'nomeSubCategoria': nomeSubCategoria
        })

    def listar_subCategoria(self):
        for subCategoria in self.subCat:
            nomeSubCategoria = subCategoria.values()
            print(' SubCategoria: ' + str(nomeSubCategoria))

subCat = SubCategorias()

while True:
    menu = int(input('\n1 - Cadastrar Novo Produto\n2 - Listar Produtos\n3 - Cadastrar Categoria\n4 - Listar Categoria\n5 - Cadastrar Subcategorias\n6 - Listar Subcategorias\n0 - Sair\n'))
    if menu == 1:
        produto.set_produto()
    elif menu == 2:
        produto.listar_produtos()
    elif menu == 3:
        categoria.cadastrar_categoria()
    elif menu == 4:
        categoria.listar_categoria()
    elif menu == 5:
        subCat.cadastrar_subCategoria()
    elif menu == 6:
        subCat.listar_subCategoria()
    elif menu == 0:
        break
    else:
        print('Não entendi!')
        continue