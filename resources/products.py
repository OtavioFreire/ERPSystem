from flask_restx import Resource, reqparse
from flask import Response
from bson import json_util


class Products(Resource):

    def get(self):

        import app

        productsGetAll = app.mongo.db.Products.find()

        resp = json_util.dumps(productsGetAll)

        return Response(resp, mimetype='application/json')

    def post(self):

        import app

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

        data = args.parse_args()
        print(data)
        if data['productCategory'] and data['productCostPrice'] and data['productEAN'] and data['productName'] and data['productProvider'] and data['productSKU'] and data['productSellPrice'] and data['productStock'] and data['productDescription']:

            data['productSKU'] = ''.join(
                filter(str.isalnum, data['productSKU']))

            print()

            idTeste = app.mongo.db.Products.estimated_document_count()

            productsFilterCount = idTeste if idTeste == 0 else app.mongo.db.Products.find(
            ).sort('id', -1).limit(1)[0]['id']
            productsFilterCount = int(productsFilterCount) + 1

            app.mongo.db.Products.insert_one(
                {'id': int(productsFilterCount),
                 'productCategory': str(data['productCategory']),
                 'productCostPrice': int(data['productCostPrice']),
                 'productEAN': int(data['productEAN']),
                 'productName': data['productName'],
                 'productProvider': data['productProvider'],
                 'productSKU': data['productSKU'],
                 'productSellPrice': int(data['productSellPrice']),
                 'productStock': int(data['productStock']),
                 'productDescription': data['productDescription']
                 }
            )

            productReturn = app.mongo.db.Products.find(
                {'id': int(productsFilterCount)})

            resp = json_util.dumps(productReturn)

            return Response(resp, mimetype='application/json')

        else:
            return {'message': 'Cannot post this product. Try again later.'}


class Product(Resource):

    def get(self, productId):

        import app

        product = app.mongo.db.Products.find({'id': productId})

        resp = json_util.dumps(product)

        return Response(resp, mimetype='application/json')

    def delete(self, productId):

        import app

        arqDelete = app.mongo.db.Products.delete_one({'id': productId})

        return {'message': 'Deletado'}

    def put(self, productId):

        import app

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

        data = args.parse_args()

        print(data['productStock'])

        productEdit = app.mongo.db.Products.find_one_and_update(
            {'id': productId},
            {'$set': {'productName': data['productName'],
                      'productSKU': data['productSKU'],
                      'productCategory': data['productCategory'],
                      'productEAN': int(data['productEAN']),
                      'productCostPrice': int(data['productCostPrice']),
                      'productSellPrice': int(data['productSellPrice']),
                      'productStock': int(data['productStock']),
                      'productProvider': data['productProvider'],
                      'productDescription': data['productDescription']
                      }, })

        resp = json_util.dumps(productEdit)

        return Response(resp, mimetype='application/json')
