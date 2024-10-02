class User:
    def __init__(self, users_id=None, name=None):
        self.__users_id = users_id
        self.__name= name
        
    def setUsers_id(self, users_id):
        self.__users_id = users_id

    def getUsers_id(self):
        return self.__users_id

    def setName(self, name):
        sef.__name = name

    def getName(self):
        return self.__name
