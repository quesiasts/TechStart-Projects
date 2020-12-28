# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask, render_template
from marketplaces import Marketplace, Category, Subcategory, Dados

app = Flask(__name__)

marketplaces = []
result_marketplaces = Dados.get_marketplaces()
for i in result_marketplaces:
    marketplaces.append(Marketplace(i['marketplaces']))

categorias = []
result_cat = Dados.get_categories()
for i in result_cat:
    for j in marketplaces:
        if i['marketplaces'] == j.get_name():
            categorias.append(Category(i['categoria'], j))

subcategorias = []
result_subcat = Dados.get_subcategories()
for i in result_subcat:
    for j in categorias:
        if i['categoria'] == j.get_name():
            subcategorias.append(Subcategory(i['subcategoria'], j))
            break

@app.route('/')
def index():
    return render_template('index.html', marketplaces = marketplaces)

@app.route('/category/<marketplaces>')
def category(mkt):
    return render_template('category.html', cat = categorias, mkt = mkt)

@app.route('/subcategory/<cat>')
def subcategory(cat):
    return render_template('subcategory.html', subcat = subcategorias, cat = cat)

app.run(debug=True)