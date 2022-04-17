from flask_restx import Resource, reqparse
from flask import Response
from bson import json_util


class Providers(Resource):

    def get(self):
        '''
            Retorna todos os providers cadastrados
        '''

        from app import mongo

        provider = mongo.db.Providers.find()

        resp = json_util.dumps(provider)

        return Response(resp, mimetype='application/json')

    def post(self):
        '''
            Retorna um novo provider apartir das informações passadas pelo RequestParser
        '''

        from app import mongo

        from resources.models.provider import ProviderModel

        args = reqparse.RequestParser()

        args.add_argument('providerName', type=str, required=True,
                          help="providerName cannot be empty.")
        args.add_argument('providerAddress', type=str, required=True,
                          help="providerAddress cannot be empty.")
        args.add_argument('providerCNPJ', type=str, required=True,
                          help="providerCNPJ cannot be empty.")
        args.add_argument('providerPhone', type=str, required=True,
                          help="providerPhone cannot be empty.")
        args.add_argument('providerRepresentative', type=str, required=True,
                          help="providerRepresentative cannot be empty.")
        args.add_argument('providerDistrict', type=str, required=True,
                          help="providerDistrict cannot be empty.")
        args.add_argument('providerState', type=str, required=True,
                          help="providerState cannot be empty.")
        args.add_argument('providerNumber', type=str, required=True,
                          help="providerNumber cannot be empty.")

        providerModel = ProviderModel(args.parse_args())

        mongo.db.Providers.insert_one(providerModel.providerNew())

        providerReturn = mongo.db.Providers.find(
            {'id': int(providerModel.id)})

        resp = json_util.dumps(providerReturn)

        return Response(resp, mimetype='application/json')


class Provider(Resource):

    def get(self, providerId):
        '''
            Retorna um provider especifico passando um providerID de referencia. 
        '''

        from app import mongo

        provider = mongo.db.Providers.find({'providerId': providerId})

        resp = json_util.dumps(provider)

        return Response(resp, mimetype='application/json')

    def delete(self, providerId):
        '''
            Deleta um provider desde que seja passado o providerID do provider que deseja deletar. 
        '''

        import app

        arqDelete = app.mongo.db.Providers.delete_one(
            {'providerId': providerId})

        return {'message': 'Deletado'}

    def put(self, providerId):
        '''
            Passando um providerID e as informações necessárias atualiza as informações no DB sobre este provider.
        '''
        import app

        from resources.models.provider import ProviderModel

        args = reqparse.RequestParser()

        args.add_argument('providerName', type=str, required=True,
                          help="providerName cannot be empty.")
        args.add_argument('providerAddress', type=str, required=True,
                          help="providerAddress cannot be empty.")
        args.add_argument('providerCNPJ', type=str, required=True,
                          help="providerCNPJ cannot be empty.")
        args.add_argument('providerPhone', type=str, required=True,
                          help="providerPhone cannot be empty.")
        args.add_argument('providerRepresentative', type=str, required=True,
                          help="providerRepresentative cannot be empty.")
        args.add_argument('providerDistrict', type=str, required=True,
                          help="providerDistrict cannot be empty.")
        args.add_argument('providerState', type=str, required=True,
                          help="providerState cannot be empty.")
        args.add_argument('providerNumber', type=str, required=True,
                          help="providerNumber cannot be empty.")

        providerModel = ProviderModel(args.parse_args())

        providerEdit = app.mongo.db.Providers.find_one_and_update(
            {'providerId': int(providerId)},
            {'$set': providerModel.putProvider()})

        resp = json_util.dumps(providerEdit)

        return Response(resp, mimetype='application/json')
