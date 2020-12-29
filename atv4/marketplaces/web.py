# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask, render_template
from marketplaces import Marketplace, Category, Subcategory, Data

app = Flask(__name__)

marketplaces = []
result_marketplaces = Data.get_marketplaces()
for i in result_marketplaces:
    marketplaces.append(Marketplace(i['marketplaces']))

categorias = []
result_cat = Data.get_categories()
for i in result_cat:
    for j in marketplaces:
        if i['marketplaces'] == j.get_name():
            categorias.append(Category(i['categoria'], j))

subcategorias = []
result_subcat = Data.get_subcat()
for i in result_subcat:
    for j in categorias:
        if i['categoria'] == j.get_name():
            subcategorias.append(Subcategory(i['subcategoria'], j))
            break

@app.route('/')
def index():
    return render_template('index.html', marketplaces = marketplaces)

@app.route('/category/<marketplaces>')
def category(marketplaces):
    print(marketplaces)
    return render_template('category.html', cat = categorias, marketplaces = marketplaces)

@app.route('/subcategory/<cat>')
def subcategory(cat):
    return render_template('subcategory.html', subcat = subcategorias, cat = cat)

app.run(debug=True)