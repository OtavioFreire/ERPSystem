from app import mongo


class UserModel:

    def __init__(self, args):
        self.name = args['name']
        self.email = args['email']
        self.password = args['password']
        self.cpf = args['cpf']
        self.birthday = args['birthday']

    def userNew(self):

        countId = mongo.db.Products.estimated_document_count()

        userFilterCount = countId if countId == 0 else mongo.db.Users.find(
        ).sort('id', -1).limit(1)[0]['id']
        userFilterCount = int(userFilterCount) + 1

        self.userId = userFilterCount

        argsJson = {'id': int(self.userId),
                    'name': str(self.name),
                    'email': str(self.email),
                    'password': str(self.password),
                    'cpf': str(self.cpf),
                    'birthday': str(self.birthday)}

        return argsJson

    def userPut(self):

        argsJson = {
            'name': str(self.name),
            'email': str(self.email),
            'password': str(self.password),
            'cpf': str(self.cpf),
            'birthday': str(self.birthday)}

        return argsJson
