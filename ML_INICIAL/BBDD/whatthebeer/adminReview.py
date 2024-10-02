#Administracion BBDD
import mysql.connector
from classReview import *
from DataSource import *

class adminReview:

    def getAll(self,dataSource):
        #Generamos la Query
        query = ("SELECT * FROM reviews")
        #Recogemos los datos que nos devuelve la consulta
        reviews_bd = dataSource.executeQuerySelect(query)
        #Creamos lista vacia para guardar objetos de las reviews
        reviews = []
        #Recorremos los datos recogidos anteriormente (matriz)
        for r in reviews_bd:
            #Creamos objetos de las reviews
            review = Review(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7])
            #Los guardamos en la lista reviews
            reviews.append(review)

        #Devolvemos la lista de objetos de reviews
        return reviews

    def getById(self,dataSource, id):
        #Generamos la Query
        query = ("SELECT * FROM reviews WHERE review_id = %i" %(id))

        #Recogemos los datos de la consulta
        reviews_bd = dataSource.executeQuerySelect(query)

        #Generamos una review como none
        review = None

        #Comprobamos que la consulta nos devuelve una fila
        if len(reviews_bd) == 1:
            #Recorremos los datos recogidos anteriormente
            for r in reviews_bd:
                #Generamos la review a partir del registro
                review = Review(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7])

        #Devolvemos la review encontrada
        return review

    def insertData(self, dataSource, review):
        #Generamos la Query
        query = ("INSERT INTO reviews VALUES (NULL,%i,%f,%f,%f,%f,%f,\"%s\")" %( review.getIdBeer(), review.getTaste(), review.getPalate(), review.getAroma(), review.getAppearance(), review.getOverall(), review.getUser_Name()))
        #Ejecutamos la query, y comprovamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def updateData(self,dataSource,review):
        #Generamos la Query
        query = ("UPDATE reviews SET beer_idbeer=%i, review_taste=%f, review_palate=%f, review_aroma=%f, review_appearance=%f, review_overall=%f, user_name='%s' WHERE review_id=%i" %(review.getIdBeer(), review.getTaste(), review.getPalate(), review.getAroma(), review.getAppearance(), review.getOverall(), review.getUser_Name(), review.getReview_id()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def deleteData(self, dataSource,review):
        #Generamos la Query
        query = ("DELETE FROM reviews WHERE review_id=%i" %(review.getReview_id()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
         
    def deleteAll(self, dataSource):
        #Generamos la Query
        query = ("DELETE FROM reviews")

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
         
        
