from app import mongo


class ProviderModel:

    def __init__(self, args):

        self.providerName = args['providerName']
        self.providerAddress = args['providerAddress']
        self.providerCNPJ = args['providerCNPJ']
        self.providerPhone = args['providerPhone']
        self.providerRepresentative = args['providerRepresentative']
        self.providerDistrict = args['providerDistrict']
        self.providerState = args['providerState']
        self.providerNumber = args['providerNumber']

    def providerNew(self):

        idTeste = mongo.db.Providers.estimated_document_count()

        providersFilterCount = idTeste if idTeste == 0 else mongo.db.Providers.find(
        ).sort('providerId', -1).limit(1)[0]['providerId']
        providersFilterCount = int(providersFilterCount) + 1

        self.id = providersFilterCount

        argsJson = {'providerId': int(providersFilterCount),
                    'providerName': str(self.providerName),
                    'providerAddress': self.providerAddress,
                    'providerCNPJ': self.providerCNPJ,
                    'providerPhone': self.providerPhone,
                    'providerRepresentative': self.providerRepresentative,
                    'providerDistrict': self.providerDistrict,
                    'providerState': self.providerState,
                    'providerNumber': self.providerNumber
                    }

        return argsJson

    def putProvider(self):

        argsJson = {
            'providerName': str(self.providerName),
            'providerAddress': self.providerAddress,
            'providerCNPJ': self.providerCNPJ,
            'providerPhone': self.providerPhone,
            'providerRepresentative': self.providerRepresentative,
            'providerDistrict': self.providerDistrict,
            'providerState': self.providerState,
            'providerNumber': self.providerNumber
        }

        return argsJson
