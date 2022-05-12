from app import mongo


class SupplierModel:

    def __init__(self, args):

        self.supplierName = args['supplierName']
        self.supplierAddress = args['supplierAddress']
        self.supplierCNPJ = args['supplierCNPJ']
        self.supplierPhone = args['supplierPhone']
        self.supplierRepresenter = args['supplierRepresenter']
        self.supplierDistrict = args['supplierDistrict']
        self.supplierState = args['supplierState']
        self.supplierNumber = args['supplierNumber']

    def supplierNew(self):

        idTeste = mongo.db.Suppliers.estimated_document_count()

        supplierFilterCount = idTeste if idTeste == 0 else mongo.db.Suppliers.find(
        ).sort('supplierId', -1).limit(1)[0]['supplierId']
        supplierFilterCount = int(supplierFilterCount) + 1

        self.id = supplierFilterCount

        argsJson = {'supplierId': int(supplierFilterCount),
                    'supplierName': str(self.supplierName),
                    'supplierAddress': self.supplierAddress,
                    'supplierCNPJ': self.supplierCNPJ,
                    'supplierPhone': self.supplierPhone,
                    'supplierRepresenter': self.supplierRepresenter,
                    'supplierDistrict': self.supplierDistrict,
                    'supplierState': self.supplierState,
                    'supplierNumber': self.supplierNumber
                    }

        return argsJson

    def putSupplier(self):

        argsJson = {
            'supplierName': str(self.supplierName),
            'supplierAddress': self.supplierAddress,
            'supplierCNPJ': self.supplierCNPJ,
            'supplierPhone': self.supplierPhone,
            'supplierRepresenter': self.supplierRepresenter,
            'supplierDistrict': self.supplierDistrict,
            'supplierState': self.supplierState,
            'supplierNumber': self.supplierNumber
        }

        return argsJson
