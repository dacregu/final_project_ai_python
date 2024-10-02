class Review:
    def __init__(self, review_id=None, idbeer=None, taste=None, palate=None, aroma=None, appearance=None, overall=None, user_name = None):
        self.__review_id = review_id
        self.__idbeer = idbeer
        self.__taste = taste
        self.__palate = palate
        self.__aroma = aroma
        self.__appearance = appearance
        self.__overall = overall
        self.__user_name = user_name

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

    def setUser_Name(self, user_name):
        self.__user_name = user_name

    def getUser_Name(self):
        return self.__user_name
