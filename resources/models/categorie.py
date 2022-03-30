from app import mongo


class CategorieModel:

    def __init__(self, args):

        self.categoryName = args['categoryName']
        self.categoryDescription = args['categoryDescription']

    def categorieNew(self):

        argsJson = {
            'categoryName':  self.categoryName,
            'categoryDescription': self.categoryDescription
        }

        return argsJson

    def categoriePost(self):

        idCount = mongo.db.Categories.estimated_document_count()

        CategoriesFilterCount = idCount if idCount == 0 else mongo.db.Categories.find(
        ).sort('id', -1).limit(1)[0]['id']
        CategoriesFilterCount = int(CategoriesFilterCount) + 1

        self.categoriesFilterCount = CategoriesFilterCount

        argsJson = {'id': CategoriesFilterCount,
                    'categoryName':  self.categoryName,
                    'categoryDescription': self.categoryDescription
                    }

        return argsJson
