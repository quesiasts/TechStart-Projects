# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask, render_template, request
from marketplaces import Marketplace, Category, Subcategory, Data

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

marketplaces = []
result_marketplaces = Data.get_marketplaces()
for i in result_marketplaces:
    marketplaces.append(Marketplace(i['marketplaces']))

categorias = []
result_cat = Data.get_categories()
for i in result_cat:
    for j in marketplaces:
        if i['marketplaces'] == j.get_name():
            categorias.append(Category(i['categories'], j))

subcategorias = []
result_subcat = Data.get_subcat()
for i in result_subcat:
    for j in categorias:
        if i['categories'] == j.get_name():
            subcategorias.append(Subcategory(i['subcategories'], j))
            break

@app.route('/')
def index():
    return render_template('index.html', marketplaces = marketplaces)

@app.route('/calcular')
def calcular():
    n1 = float(request.args.get('num1'))
    n2 = float(request.args.get('num2'))
    operacao = request.args.get('operacao')
    if operacao == 'somar':
        resultado = soma(n1, n2)
    elif operacao == 'subtrair':
        resultado = subtracao(n1, n2)
    elif operacao == 'multiplicar':    
        resultado = multiplicacao(n1, n2)
    elif operacao == 'dividir':
        resultado = divisao(n1, n2)
    else:
        return 'Operação invalida'
    return f'O resultado da {operacao} entre {n1} e {n2} é {resultado}' 

@app.route('/category/<marketplaces>')
def category(marketplaces):
    print(marketplaces)
    return render_template('category.html', cat = categorias, marketplaces = marketplaces)

@app.route('/subcategory/<cat>')
def subcategory(cat):
    return render_template('subcategory.html', subcat = subcategorias, cat = cat)

app.run(debug=True)