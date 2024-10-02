class Beer:
    def __init__(self, beer_id=None, brewery_id=None, name=None, style=None, abv=None):
        self.__beer_id = beer_id
        self.__brewery_id = brewery_id
        self.__name = name
        self.__style = style
        self.__abv = abv

    def setBeer_id(self, beer_id):
        self.__beer_id = beer_id

    def getBeer_id(self):
        return self.__beer_id

    def setBrewery_id(self, brewery_id):
        self.__brewery_id = brewery_id

    def getBrewery_id(self):
        return self.__brewery_id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setStyle(self, style):
        self.__style = style

    def getStyle(self):
        return self.__style

    def setAbv(self, abv):
        self.__abv = abv

    def getAbv(self):
        return self.__abv
