class Correlation:
    def __init__(self, beer_id=None, beer_idcorr=None,correlation=None):
        self.__beer_id = beer_id
        self.__beer_idcorr = beer_idcorr
        self.__correlation = correlation

    def setBeer_id(self, beer_id):
        self.__beer_id = beer_id

    def getBeer_id(self):
        return self.__beer_id

    def setBeer_idcorr(self, beer_idcorr):
        self.__beer_id = beer_idcorr

    def getBeer_idcorr(self):
        return self.__beer_idcorr

    def setCorrelation(self, correlation):
        self.__correlation = correlation

    def getCorrelation(self):
        return self.__correlation


       
    
   
