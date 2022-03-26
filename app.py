#   cmd
#   .\venv\Scripts\activate.bat
#   pip install -r requirements.txt

from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_pymongo import PyMongo
from resources import products

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['MONGO_URI'] = "mongodb+srv://redadmin:1234@cluster0.euics.mongodb.net/ERPSystem?retryWrites=true&w=majority"
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)
mongo = PyMongo(app)

api.add_resource(products.Products, '/product/')

if __name__ == '__main__':
    app.run(debug=True)
