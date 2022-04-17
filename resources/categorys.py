from flask_restx import Resource, reqparse
from flask import Response
from bson import json_util


class Category(Resource):

    def get(self, categoryId):
        '''
            Retorna um categoria especifico passando um categoryID de referencia. 
        '''
        from app import mongo

        category = mongo.db.Categories.find({'id': categoryId})

        resp = json_util.dumps(category)

        return Response(resp, mimetype='application/json')

    def delete(self, categoryId):
        '''
            Deleta um categoria desde que seja passado o categoryID do produto que deseja deletar. 
        '''
        from app import mongo

        mongo.db.Categories.delete_one({'id': categoryId})

        return {'message': 'This category has been deleted.'}

    def put(self, categoryId):
        '''
            Passando um categoryID e as informações necessárias atualiza as informações no DB sobre esta categoria.
        '''
        from app import mongo
        from resources.models.categorie import CategorieModel

        args = reqparse.RequestParser()

        args.add_argument('categoryName', type=str, required=True,
                          help="categoryName cannot be empty.")
        args.add_argument('categoryDescription', type=str, required=True,
                          help="categoryDescription cannot be empty.")

        categorieModel = CategorieModel(args.parse_args())

        categoryEdit = mongo.db.Categories.find_one_and_update(
            {'id': categoryId},
            {'$set': categorieModel.categorieNew(), })

        resp = json_util.dumps(categoryEdit)

        return Response(resp, mimetype='application/json')


class Categories(Resource):
    def get(self):
        '''
            Retorna todas as categorias existentes no DB. 
        '''
        from app import mongo

        categoriesGetAll = mongo.db.Categories.find()
        resp = json_util.dumps(categoriesGetAll)

        return Response(resp, mimetype='application/json')

    def post(self):
        '''
            Cria uma categoria nova passando os atributos necessários.
        '''
        from app import mongo
        from resources.models.categorie import CategorieModel

        args = reqparse.RequestParser()
        args.add_argument('categoryName', type=str, required=True,
                          help="categoryName cannot be empty.")
        args.add_argument('categoryDescription', type=str, required=True,
                          help="categoryDescription cannot be empty.")

        categorieModel = CategorieModel(args.parse_args())

        mongo.db.Categories.insert_one(categorieModel.categoriePost())

        CategoryReturn = mongo.db.Categories.find(
            {'id': int(categorieModel.categoriesFilterCount)})

        resp = json_util.dumps(CategoryReturn)

        return Response(resp, mimetype='application/json')
