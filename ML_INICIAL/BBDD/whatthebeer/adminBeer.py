#Administracion BBDD
import mysql.connector
from classBeer import *
from DataSource import *

class adminBeer:

    def getAll(self,dataSource):
        #Generamos la Query
        query = ("SELECT * FROM beers")
        #Recogemos los datos que nos devuelve la consulta
        beers_bd = dataSource.executeQuerySelect(query)
        #Creamos lista vacia para guardar objetos de las cervezas
        beers = []
        #Recorremos los datos recogidos anteriormente (matriz)
        for b in beers_bd:
            #Creamos objetos de las cervezas
            beer = Beer(b[0],b[1],b[2],b[3],b[4])
            #Los guardamos en la lista beers
            beers.append(beer)

        #Devolvemos la lista de objetos de cervezas
        return beers

    def getEstilos(self,dataSource):
        #Generamos la Query
        query = ("SELECT beer_style FROM beers GROUP BY beer_style")
        #Recogemos los datos que nos devuelve la consulta
        beers_bd = dataSource.executeQuerySelect(query)
        #Creamos lista vacia para guardar objetos de las cervezas
        beers = []
        #Recorremos los datos recogidos anteriormente (matriz)
        for b in beers_bd:
            #Creamos objetos de las cervezas
            beer = Beer(style = b[0])
            #Los guardamos en la lista beers
            beers.append(beer)

        #Devolvemos la lista de objetos de cervezas
        return beers

    def getById(self,dataSource, id):
        #Generamos la Query
        query = ("SELECT * FROM beers WHERE beer_beerid = %i" %(id))

        #Recogemos los datos de la consulta
        beers_bd = dataSource.executeQuerySelect(query)

        #Generamos una cerveza como none
        beer = None

        #Comprobamos que la consulta nos devuelve una fila
        if len(beers_bd) == 1:
            #Recorremos los datos recogidos anteriormente
            for b in beers_bd:
                #Generamos la cerveza a partir del registro
                beer = Beer(b[0],b[1],b[2],b[3],b[4])

        #Devolvemos la cerveza encontrada
        return beer

    def insertData(self, dataSource, beer):
        #Generamos la Query
        beer.setName(beer.getName().replace("\"","'"))
        beer.setStyle(beer.getStyle().replace("\"","'"))
        query = ("INSERT INTO beers VALUES (%i,%i,\"%s\",\"%s\",%f)" %(beer.getBeer_id(),beer.getBrewery_id(),beer.getName(),beer.getStyle(),beer.getAbv()))
        #Ejecutamos la query, y comprovamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def updateData(self,dataSource,beer):
        #Generamos la Query
        query = ("UPDATE beers SET brewery_id=%i, beer_name='%s', beer_style='%s', beer_abv=%f WHERE beer_beerid=%i" %(beer.getBrewery_id(),beer.getName(),beer.getStyle(),beer.getAbv(),beer.getBeer_id()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def deleteData(self, dataSource,beer):
        #Generamos la Query
        query = ("DELETE FROM beers WHERE beer_beerid=%i" %(beer.getBeer_id()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
        
    def deleteAll(self, dataSource):
        #Generamos la Query
        query = ("DELETE FROM beers")

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
        
        
