#Administracion BBDD
import mysql.connector
from classCorrelation import *
from DataSource import *

class adminCorrelation:

    def getAll(self,dataSource):
        #Generamos la Query
        query = ("SELECT * FROM correlation")
        #Recogemos los datos que nos devuelve la consulta
        correlations_bd = dataSource.executeQuerySelect(query)
        #Creamos lista vacia para guardar objetos de las correlations
        correlations = []
        #Recorremos los datos recogidos anteriormente (matriz)
        for c in correlations_bd:
            #Creamos objetos de las correlations
            correlation = Correlation(c[0],c[1],c[2])
            #Los guardamos en la lista correlations
            correlations.append(correlation)

        #Devolvemos la lista de objetos de correlaciones
        return correlations            

    def getById(self,dataSource, id):
        #Generamos la Query
        query = ("SELECT * FROM correlation WHERE beer_id=%i OR beer_idcorr=%i" %(id,id))

        #Recogemos los datos de la consulta
        correlations_bd = dataSource.executeQuerySelect(query)

        #Creamos lista vacia para guardar objetos de las correlations
        correlations = []

        #Recorremos los datos recogidos anteriormente
        for c in correlations_bd:
            #Creamos objetos de las correlations
            correlation = Correlation(c[0],c[1],c[2])
            #Los guardamos en la lista correlations
            correlations.append(correlation)

        #Devolvemos la lista de objetos de correlaciones
        return correlations  

    def getByIds(self,dataSource, beer_id, beer_idcorr):
        #Generamos la Query
        query = ("SELECT * FROM correlation WHERE beer_id=%i AND beer_idcorr=%i" %(beer_id,beer_idcorr))
        #Recogemos los datos de la consulta
        correlations_bd = dataSource.executeQuerySelect(query)

        #Creamos lista vacia para guardar objetos de las correlations
        correlation = None

        #Comprobamos que la consulta nos devuelve una fila
        if len(correlations_bd) == 1:
            #Recorremos los datos recogidos anteriormente
            for c in correlations_bd:
                #Creamos objetos de las correlations
                correlation = Correlation(c[0],c[1],c[2])

        #Devolvemos la lista de objetos de correlaciones
        return correlation  

    def insertData(self, dataSource, correlation):
        #Generamos la Query
        query = ("INSERT INTO correlation VALUES (%i,%i,%f)" %(correlation.getBeer_id(), correlation.getBeer_idcorr(), correlation.getCorrelation()))

        #Ejecutamos la query, y comprovamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def updateData(self,dataSource, correlation):
        #Generamos la Query
        query = ("UPDATE correlation SET correlation=%f WHERE beer_id=%i AND beer_idcorr=%i" %(correlation.getCorrelation(), correlation.getBeer_id(), correlation.getBeer_idcorr()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def deleteData(self, dataSource, correlation):
        #Generamos la Query
        query = ("DELETE FROM correlation WHERE beer_id=%i AND beer_idcorr=%i" %(correlation.getBeer_id(), correlation.getBeer_idcorr()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
         
    def deleteAll(self, dataSource):
        #Generamos la Query
        query = ("DELETE FROM correlation")

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
         
