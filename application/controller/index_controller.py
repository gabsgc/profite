from application import app
from flask import render_template, request
from application.model.dao.product_dao import ProductDAO

product_list = ProductDAO().listarTodos()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', product_list = product_list)

@app.route('/list', methods=['GET'])
def listaProduct():
    return render_template('product.html', product_list = product_list)