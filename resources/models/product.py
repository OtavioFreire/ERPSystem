from app import mongo


class ProductModel:

    def __init__(self, args):

        self.productName = args['productName']
        self.productSKU = args['productSKU']
        self.productCategory = args['productCategory']
        self.productEAN = args['productEAN']
        self.productCostPrice = args['productCostPrice']
        self.productSellPrice = args['productSellPrice']
        self.productStock = args['productStock']
        self.productProvider = args['productProvider']
        self.productDescription = args['productDescription']

    def productNew(self):

        idTeste = mongo.db.Products.estimated_document_count()

        productsFilterCount = idTeste if idTeste == 0 else mongo.db.Products.find(
        ).sort('id', -1).limit(1)[0]['id']
        productsFilterCount = int(productsFilterCount) + 1

        self.id = productsFilterCount

        argsJson = {'id': int(productsFilterCount),
                    'productCategory': str(self.productCategory),
                    'productCostPrice': int(self.productCostPrice),
                    'productEAN': int(self.productEAN),
                    'productName': self.productName,
                    'productProvider': self.productProvider,
                    'productSKU': self.productSKU,
                    'productSellPrice': int(self.productSellPrice),
                    'productStock': int(self.productStock),
                    'productDescription': self.productDescription
                    }

        return argsJson

    def putProduct(self):

        argsJson = {
            'productCategory': str(self.productCategory),
            'productCostPrice': int(self.productCostPrice),
            'productEAN': int(self.productEAN),
            'productName': self.productName,
            'productProvider': self.productProvider,
            'productSKU': self.productSKU,
            'productSellPrice': int(self.productSellPrice),
            'productStock': int(self.productStock),
            'productDescription': self.productDescription
        }

        return argsJson
