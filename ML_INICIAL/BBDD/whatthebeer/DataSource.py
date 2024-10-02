import mysql.connector

class DataSource:
        #Constructor, este inicia la conexion con a BBDD y desactiva el comit automatico
        def __init__(self):
                self.__cnx = mysql.connector.connect(user='whatthebeer',password='whatthebeer1234%',host='localhost', database='wtb')
                self.__cnx.autocommit = False

	#Funcion que recoge el ultimo ID insertado o modificado en la BBDD	
        def getLastID(cursor):
                return self.__cnx.insert_id()

    #Funcion que ciera la conexion con la BBDD
        def closeConexion(self):
                self.__cnx.close()
    
    #Funcion para ejecutar consultas select, ya que queremos que devuelvan los datos
        def executeQuerySelect(self, query):
                #Se genera el cursor
                cursor = self.__cnx.cursor()
		#Se ejecuta Querry.
                cursor.execute(query)
		#Se recoge los datos que nos devuelve la consulta
                result = cursor.fetchall()
		#Se cierra cursor
                cursor.close()
		#Se devuelve el resultado
                return result

        def executeOtherQuery(self, query):
                #Se genera el cursor
                cursor = self.__cnx.cursor()
                #Se ejecuta Querry.
                cursor.execute(query)
		#Se cierra el cursor
                cursor.close()
		#Se devuelve True"
                return True

	#funcion para realizar el commit con la BBDD
        def commitAction(self):
                self.__cnx.commit()

	#Funcion que hace roolnack en la BBDD
        def rollbackAction(self):
                self.__cnx.rollback()
                
