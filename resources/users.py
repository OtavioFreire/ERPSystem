from itertools import product
from flask_restx import Resource, reqparse
from flask import Response
from bson import json_util

from resources.products import Product


class Users(Resource):

    def get(self):
        '''
            Retorna todos os usuarios cadastrados
        '''

        from app import mongo

        usersGetAll = mongo.db.Users.find()

        resp = json_util.dumps(usersGetAll)

        return Response(resp, mimetype='application/json')

    def post(self):
        '''
            Retorna um novo user apartir das informações passadas pelo RequestParser
        '''

        from app import mongo

        from resources.models.user import UserModel

        args = reqparse.RequestParser()

        args.add_argument('name', type=str, required=True,
                          help="Name cannot be empty")

        args.add_argument('email', type=str, required=True,
                          help="email cannot be empty")

        args.add_argument('password', type=str, required=True,
                          help="password cannot be empty")

        args.add_argument('cpf', type=str, required=True,
                          help="cpf cannot be empty")

        args.add_argument('birthday', type=str, required=True,
                          help="birthday cannot be empty")

        userModel = UserModel(args.parse_args())

        mongo.db.Users.insert_one(userModel.userNew())

        userReturn = mongo.db.Users.find(
            {'id': userModel.userId}
        )

        resp = json_util.dumps(userReturn)

        return Response(resp, mimetype='application/json')


class User(Resource):

    def get(self, userId):
        '''
            Retorna um produto especifico passando um userId de referencia. 
        '''

        from app import mongo

        resp = json_util.dumps(mongo.db.Users.find({'id': userId}))

        return Response(resp, mimetype='application/json')
