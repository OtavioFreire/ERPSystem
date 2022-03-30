from flask_restx import Resource, reqparse
from flask import Response
from bson import json_util


class Category(Resource):

    def get(self, categoryId):

        from app import mongo

        category = mongo.db.Categories.find({'id': categoryId})

        resp = json_util.dumps(category)

        return Response(resp, mimetype='application/json')

    def delete(self, categoryId):

        from app import mongo

        mongo.db.Categories.delete_one({'id': categoryId})

        return {'message': 'This category has been deleted.'}

    def put(self, categoryId):

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

        from app import mongo

        categoriesGetAll = mongo.db.Categories.find()
        resp = json_util.dumps(categoriesGetAll)

        return Response(resp, mimetype='application/json')

    def post(self):
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
