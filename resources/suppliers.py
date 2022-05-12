from flask_restx import Resource, reqparse
from flask import Response
from bson import json_util


class Suppliers(Resource):

    def get(self):
        '''
            Retorna todos os suppliers cadastrados
        '''

        from app import mongo

        provider = mongo.db.Suppliers.find()

        resp = json_util.dumps(provider)

        return Response(resp, mimetype='application/json')

    def post(self):
        '''
            Retorna um novo provider apartir das informações passadas pelo RequestParser
        '''

        from app import mongo

        from resources.models.supplier import SupplierModel

        args = reqparse.RequestParser()

        args.add_argument('supplierName', type=str, required=True,
                          help="supplierName cannot be empty.")
        args.add_argument('supplierAddress', type=str, required=True,
                          help="supplierAddress cannot be empty.")
        args.add_argument('supplierCNPJ', type=str, required=True,
                          help="supplierCNPJ cannot be empty.")
        args.add_argument('supplierPhone', type=str, required=True,
                          help="supplierPhone cannot be empty.")
        args.add_argument('supplierRepresenter', type=str, required=True,
                          help="supplierRepresenter cannot be empty.")
        args.add_argument('supplierDistrict', type=str, required=True,
                          help="supplierDistrict cannot be empty.")
        args.add_argument('supplierState', type=str, required=True,
                          help="supplierState cannot be empty.")
        args.add_argument('supplierNumber', type=str, required=True,
                          help="supplierNumber cannot be empty.")

        supplierModel = SupplierModel(args.parse_args())

        mongo.db.Suppliers.insert_one(supplierModel.supplierNew())

        supplierReturn = mongo.db.Suppliers.find(
            {'supplierId': int(supplierModel.id)})

        resp = json_util.dumps(supplierReturn)

        return Response(resp, mimetype='application/json')


class Supplier(Resource):

    def get(self, supplierId):
        '''
            Retorna um supplier especifico passando um supplierId de referencia. 
        '''

        from app import mongo

        supplier = mongo.db.Suppliers.find({'supplierId': supplierId})

        resp = json_util.dumps(supplier)

        return Response(resp, mimetype='application/json')

    def delete(self, supplierId):
        '''
            Deleta um supplier desde que seja passado o supplierId do supplier que deseja deletar. 
        '''

        import app

        arqDelete = app.mongo.db.Suppliers.delete_one(
            {'supplierId': supplierId})

        return {'message': 'Deletado'}

    def put(self, supplierId):
        '''
            Passando um supplierId e as informações necessárias atualiza as informações no DB sobre este Suppliers.
        '''
        import app

        from resources.models.supplier import SupplierModel

        args = reqparse.RequestParser()

        args.add_argument('supplierName', type=str, required=True,
                          help="supplierName cannot be empty.")
        args.add_argument('supplierAddress', type=str, required=True,
                          help="supplierAddress cannot be empty.")
        args.add_argument('supplierCNPJ', type=str, required=True,
                          help="supplierCNPJ cannot be empty.")
        args.add_argument('supplierPhone', type=str, required=True,
                          help="supplierPhone cannot be empty.")
        args.add_argument('supplierRepresenter', type=str, required=True,
                          help="supplierRepresenter cannot be empty.")
        args.add_argument('supplierDistrict', type=str, required=True,
                          help="supplierDistrict cannot be empty.")
        args.add_argument('supplierState', type=str, required=True,
                          help="supplierState cannot be empty.")
        args.add_argument('supplierNumber', type=str, required=True,
                          help="supplierNumber cannot be empty.")

        supplierModel = SupplierModel(args.parse_args())

        supplierEdit = app.mongo.db.Suppliers.find_one_and_update(
            {'supplierId': int(supplierId)},
            {'$set': supplierModel.putSupplier()})

        resp = json_util.dumps(supplierEdit)

        return Response(resp, mimetype='application/json')
