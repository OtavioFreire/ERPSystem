#   cmd
#   .\venv\Scripts\activate.bat
#   pip install -r requirements.txt

from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_pymongo import PyMongo
from resources.categorys import Categories, Category
from resources.products import Products, Product


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['MONGO_URI'] = "mongodb+srv://redadmin:1234@cluster0.euics.mongodb.net/ERPSystem?retryWrites=true&w=majority"
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)
mongo = PyMongo(app)

api.add_resource(Products, '/product/')
api.add_resource(Product, '/product/<int:productId>')
api.add_resource(Categories, '/category/')
api.add_resource(Category, '/category/<int:categoryId>')


if __name__ == '__main__':
    app.run(debug=True)
