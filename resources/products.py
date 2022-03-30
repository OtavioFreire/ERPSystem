from flask_restx import Resource, reqparse
from flask import Response
from bson import json_util


class Products(Resource):

    def get(self):

        from app import mongo

        productsGetAll = mongo.db.Products.find()

        resp = json_util.dumps(productsGetAll)

        return Response(resp, mimetype='application/json')

    def post(self):

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

        mongo.db.Products.insert_one(productModel.getProduct())

        productReturn = mongo.db.Products.find(
            {'id': int(productModel.id)})

        resp = json_util.dumps(productReturn)

        return Response(resp, mimetype='application/json')


class Product(Resource):

    def get(self, productId):

        from app import mongo

        product = mongo.db.Products.find({'id': productId})

        resp = json_util.dumps(product)

        return Response(resp, mimetype='application/json')

    def delete(self, productId):

        import app

        arqDelete = app.mongo.db.Products.delete_one({'id': productId})

        return {'message': 'Deletado'}

    def put(self, productId):

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
