#Administracion BBDD
import mysql.connector
from classUser import *
from DataSource import *

class adminUser:

    def getAll(self,dataSource):
        #Generamos la Query
        query = ("SELECT * FROM users")
        #Recogemos los datos que nos devuelve la consulta
        users_bd = dataSource.executeQuerySelect(query)
        #Creamos lista vacia para guardar objetos de los usuarios
        users = []
        #Recorremos los datos recogidos anteriormente (matriz)
        for u in users_bd:
            #Creamos objetos de los usuarios
            user = User(u[0],u[1])
            #Los guardamos en la lista users
            users.append(user)

        #Devolvemos la lista de objetos de usuarios
        return users

    def getById(self,dataSource, id):
        #Generamos la Query
        query = ("SELECT * FROM users WHERE users_id = %i" %(id))

        #Recogemos los datos de la consulta
        users_bd = dataSource.executeQuerySelect(query)

        #Generamos un usuario como none
        user = None

        #Comprobamos que la consulta nos devuelve una fila
        if len(users_bd) == 1:
            #Recorremos los datos recogidos anteriormente
            for u in users_bd:
                #Generamos el usuario a partir del registro
                user = User(u[0],u[1])

        #Devolvemos el usuario encontrada
        return user

    def insertData(self, dataSource, user):
        #Generamos la Query
        query = ("INSERT INTO users VALUES (%i,'%s')" %(user.getUsers_id(), user.getName()))

        #Ejecutamos la query, y comprovamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def updateData(self,dataSource,user):
        #Generamos la Query
        query = ("UPDATE users SET name='%s' WHERE users_id=%i" %(user.getName(), user.getUsers_id()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)

    def deleteData(self, dataSource,user):
        #Generamos la Query
        query = ("DELETE FROM users WHERE users_id=%i" %(user.getUsers_id()))

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
          
    def deleteAll(self, dataSource):
        #Generamos la Query
        query = ("DELETE FROM users")

        #Ejecutamos la query, y comprobamos que todo haya salido bien
        return dataSource.executeOtherQuery(query)
         
               
