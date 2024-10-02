#Administracion BBDD
import mysql.connector
from classBrewery import *
from DataSource import *

class adminBrewery:

    def getAll(self,dataSource):
        #Generamos la Query
        query = ("SELECT * FROM breweries")
        #Recogemos los datos que nos devuelve la consulta
        breweries_bd = dataSource.executeQuerySelect(query)
        #Creamos lista vacia para guardar objetos de las breweries
        breweries = []
        #Recorremos los datos recogidos anteriormente (matriz)
        for b in breweries_bd:
            #Creamos objetos de las breweries
            brewery = Brewery(b[0],b[1])
            #Los guardamos en la lista breweries
            breweries.append(brewery)

        #Devolvemos la lista de objetos de breweries
        return breweries

    def getById(self,dataSource, id):
        #Generamos la Query
        query = ("SELECT * FROM breweries WHERE brewery_id = %i" %(id))

        #Recogemos los datos de la consulta
        breweries_bd = dataSource.executeQuerySelect(query)

        #Generamos una brewery como none
        brewery = None

        #Comprobamos que la consulta nos devuelve una fila
        if len(breweries_bd) == 1:
            #Recorremos los datos recogidos anteriormente
            for b in breweries_bd:
                #Generamos la brewery a partir del registro
                brewery = Brewery(b[0],b[1])

        #Devolvemos la brewery encontrada
        return brewery

    def insertData(self, dataSource, brewery):
        #Generamos la Query
        query = ("INSERT INTO breweries VALUES (%i,'%s')" %(brewery.getBrewery_id(), brewery.getBrewery_name()))

        #Ejecutamos la query, y comprovamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def updateData(self,dataSource,brewery):
        #Generamos la Query
        query = ("UPDATE breweries SET brewery_name='%s' WHERE brewery_id=%i" %(brewery.getBrewery_name(), brewery.getBrewery_id()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def deleteData(self, dataSource,brewery):
        #Generamos la Query
        query = ("DELETE FROM breweries WHERE brewery_id=%i" %(brewery.getBrewery_id()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
         
    def deleteAll(self, dataSource):
        #Generamos la Query
        query = ("DELETE FROM breweries")

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
         
