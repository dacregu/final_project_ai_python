class Review:
    def __init__(self, review_id=None, idbeer=None, taste=None, palate=None, aroma=None, appearance=None, overall=None, users_id = None):
        self.__review_id = review_id
        self.__idbeer = idbeer
        self.__taste = taste
        self.__palate = palate
        self.__aroma = aroma
        self.__appearance = appearance
        self.__overall = overall
        self.__users_id = users_id

    def setReview_id(self, review_id):
        self.__review_id = review_id

    def getReview_id(self):
        return self.__review_id

    def setIdBeer(self, idbeer):
        self.__idbeer = idbeer

    def getIdBeer(self):
        return self.__idbeer

    def setTaste(self, taste):
        self.__taste = taste

    def getTaste(self):
        return self.__taste

    def setPalate(self, palate):
        self.__palate = palate

    def getPalate(self):
        return self.__palate

    def setAroma(self, aroma):
        self.__aroma = aroma

    def getAroma(self):
        return self.__aroma

    def setAppearance(self, appearance):
        self.__appearance = appearance

    def getAppearance(self):
        return self.__appearance

    def setOverall(self, overall):
        self.__overall = overall

    def getOverall(self):
        return self.__overall

    def setUsers_Id(self, users_id):
        self.__users_id = users_id

    def getUsers_Id(self):
        return self.__users_id
