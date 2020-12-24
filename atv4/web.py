# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask, render_template
from marketplaces import Marketplace, Category, Subcategory

app = Flask(__name__)

marketplaces = [Marketplace('Amazon'), Marketplace('B2W'), Marketplace('Mercado Livre'), Marketplace('Via Varejo'), Marketplace('Sair')]
categorias = [Category('Móveis', marketplaces[1]), Category('Telefonia', marketplaces[0]), Category('Eletrodomésticos', marketplaces[1]), Category('Informática', marketplaces[1])]
subcategorias = [Subcategory('Cama', categorias[0]), Subcategory('Cadeira', categorias[0]), Subcategory('Mesa', categorias[1])]


@app.route('/')
def index():
    return render_template('index.html', marketplaces = marketplaces)

@app.route('/category/<mkt>')
def category(mkt):
    return render_template('category.html', cat = categorias, mkt = mkt)


app.run(debug=True)