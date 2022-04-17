#   cmd
#   .\venv\Scripts\activate.bat
#   pip install -r requirements.txt

from flask import Flask
from flask_restx import Api, fields
from flask_cors import CORS
from flask_pymongo import PyMongo
from resources.categorys import Categories, Category
from resources.products import Products, Product
from resources.providers import Providers, Provider

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['MONGO_URI'] = "mongodb+srv://redadmin:1234@cluster0.euics.mongodb.net/ERPSystem?retryWrites=true&w=majority"
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app, title='ERPSystem')

mongo = PyMongo(app)


ns_product = api.namespace('product',
                           description='Todas requisições referente ao endpoint Product')

ns_category = api.namespace('category',
                            description='Todas requisições referente ao endpoint Category')

ns_provider = api.namespace('provider',
                            description='Todas requisições referente ao endpoint Provider')

ns_product.add_resource(Products, '/')
ns_product.add_resource(Product, '/<int:productId>')
ns_category.add_resource(Categories, '/')
ns_category.add_resource(Category, '/<int:categoryId>')
ns_provider.add_resource(Providers, '/')
ns_provider.add_resource(Provider, '/<int:providerId>')


if __name__ == '__main__':
    app.run(debug=True)
