from flask_restx import Resource, reqparse
from flask import Response
from bson import json_util


class Products(Resource):

    def get(self):
        '''
            Retorna todos os produtos cadastrados. 
        '''

        from app import mongo

        productsGetAll = mongo.db.Products.find()

        resp = json_util.dumps(productsGetAll)

        return Response(resp, mimetype='application/json')

    def post(self):
        '''
            Retorna um novo produto apartir das informações passadas pelo RequestParser
        '''

        from app import mongo

        from resources.models.product import ProductModel

        args = reqparse.RequestParser()

        args.add_argument('productName', type=str, required=True,
                          help="productName cannot be empty.")
        args.add_argument('productSKU', type=str, required=True,
                          help="productSKU cannot be empty.")
        args.add_argument('productCategory', type=str, required=True,
                          help="productCategory cannot be empty.")
        args.add_argument('productEAN', type=str, required=True,
                          help="productEAN cannot be empty.")
        args.add_argument('productCostPrice', type=str, required=True,
                          help="productCostPrice cannot be empty.")
        args.add_argument('productSellPrice', type=str, required=True,
                          help="productSellPrice cannot be empty.")
        args.add_argument('productStock', type=str, required=True,
                          help="productStock cannot be empty.")
        args.add_argument('productProvider', type=str, required=True,
                          help="productProvider cannot be empty.")
        args.add_argument('productDescription', type=str, required=True,
                          help="productDescription cannot be empty.")

        productModel = ProductModel(args.parse_args())

        mongo.db.Products.insert_one(productModel.productNew())

        productReturn = mongo.db.Products.find(
            {'id': int(productModel.id)})

        resp = json_util.dumps(productReturn)

        return Response(resp, mimetype='application/json')


class Product(Resource):

    def get(self, productId):
        '''
            Retorna um produto especifico passando um productID de referencia. 
        '''

        from app import mongo

        product = mongo.db.Products.find({'id': productId})

        resp = json_util.dumps(product)

        return Response(resp, mimetype='application/json')

    def delete(self, productId):
        '''
            Deleta um produto desde que seja passado o productID do produto que deseja deletar. 
        '''

        import app

        arqDelete = app.mongo.db.Products.delete_one({'id': productId})

        return {'message': 'Deletado'}

    def put(self, productId):
        '''
            Passando um productID e as informações necessárias atualiza as informações no DB sobre este produto.
        '''
        import app

        from resources.models.product import ProductModel

        args = reqparse.RequestParser()

        args.add_argument('productName', type=str, required=True,
                          help="productName cannot be empty.")
        args.add_argument('productSKU', type=str, required=True,
                          help="productSKU cannot be empty.")
        args.add_argument('productCategory', type=str, required=True,
                          help="productCategory cannot be empty.")
        args.add_argument('productEAN', type=str, required=True,
                          help="productEAN cannot be empty.")
        args.add_argument('productCostPrice', type=str, required=True,
                          help="productCostPrice cannot be empty.")
        args.add_argument('productSellPrice', type=str, required=True,
                          help="productSellPrice cannot be empty.")
        args.add_argument('productStock', type=str, required=True,
                          help="productStock cannot be empty.")
        args.add_argument('productProvider', type=str, required=True,
                          help="productProvider cannot be empty.")
        args.add_argument('productDescription', type=str)

        productModel = ProductModel(args.parse_args())

        productEdit = app.mongo.db.Products.find_one_and_update(
            {'id': productId},
            {'$set': productModel.putProduct()})

        resp = json_util.dumps(productEdit)

        return Response(resp, mimetype='application/json')
