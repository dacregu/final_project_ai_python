#Se importa la librería pandas
import pandas as pd
import numpy as np
import json
import os
import sys
import math
import operator
sys.path.insert(1, './BBDD/whatthebeer')
from DataSource import *
from adminBeer import *
from classBeer import *
from adminReview import *
from classReview import *
from adminCorrelation import *
from classCorrelation import *

#Creamos la clase recomendaciones
class Recomendaciones():
#Constructor
    def __init__(self):
        #quitaestamierdalalalaself._rutaHome = "C:\\Users\\diego\\Documents\\proyecto_finalai\\proyecto_finalai\\ML_INICIAL"
        self._rutaHome = os.getcwd()
        self._filteredRatings = None

    def leerYfiltrar(self,qty):
        # Leemos los archivos
        print('LEYENDO DATOS..')
        ratings = pd.read_csv(self._rutaHome + '\\datos\\beer_reviews.csv', sep=',')

        # Eliminamos las columnas innecesarias
        del ratings['review_time']

        # recorte TESTER
        ratings = ratings[:qty]

        # Seleccionamos minimas reviews por usuario:
        # seleccionamos 8(66% de los datos cascan), para el 3er quartil es 16 (75% de los datos cascan)
        # print('3rd quartile:',np.percentile(ratings.groupby(ratings.review_profilename).count()['beer_beerid'].values,75))
        print('FILTRANDO DATOS..')
        min_reviews = 8

        # esto devuelve |user|true/false|
        group_user = ratings.groupby(ratings.review_profilename).count()['beer_beerid'] >= min_reviews

        # creamos contadores
        counter_usuariosGuardados = 0
        counter_usuariosEliminados = 0

        # eliminamos los usuarios que han puntuado menos de 'min_reviews' veces
        for key, value in group_user.items():
            if value:
                counter_usuariosGuardados += 1
            else:
                ratings = ratings[ratings.review_profilename != key]
                counter_usuariosEliminados += 1
        print("    usuarios", "guardados:", counter_usuariosGuardados, "    eliminados:", counter_usuariosEliminados)
        print("GUARDANDO ARCHIVOS..")
        # variable de clase
        self._filteredRatings = ratings

        # guardamos copia en json por si acaso
        ##ratings = ratings.to_json(self._rutaHome+'\\datos\\datosFiltrados.json',orient='index')

    def paBeers(self):
        ###Data frame filtrado y agrupado para meter en BD
        group_beerid = self._filteredRatings.groupby(["beer_beerid", "brewery_id", "beer_name", \
                                                      "beer_style", "beer_abv"])["review_overall"].mean()

        # creamos objeto data source, para la BDD
        dataSource1 = DataSource()
        adminCorrelation1 = adminCorrelation()
        adminBeer1 = adminBeer()
        adminReview1 = adminReview()

        # vaciamso BDD
        adminReview1.deleteAll(dataSource1)
        adminCorrelation1.deleteAll(dataSource1)
        adminBeer1.deleteAll(dataSource1)

        # metemos cada cerveza en la BD
        try:
            print('    INICIO BUCLE GUARDAR')
            # no hay mas inserts, pero funciona bien
            longitud = len(group_beerid.index)
            for i in range(0, longitud):
                # print(group_beerid.index[i])

                beer = Beer(group_beerid.index[i][0], group_beerid.index[i][1], group_beerid.index[i][2], \
                            group_beerid.index[i][3], group_beerid.index[i][4], )
                adminBeer1.insertData(dataSource1, beer)
            # DESPUES q acaben los inserts hacemos el commit
            dataSource1.commitAction()
            print('    FIN BUCLE GUARDAR')
        # se podrian poner distintos tipos de except , pj para saltar si ya esta añadido en vez q pete
        except Exception as e:
            # si peta se quita to lo que habia antes del ultimo commit
            dataSource1.rollbackAction()
            print(e, '    EXCEPTION!')
        finally:
            # cerramos la conexion con la base
            dataSource1.closeConexion()
            print('    FINALIZADO TRY') #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!limpiar estos pirnts

    def guardarFiltrado(self):
        # pillamos la variable, luego ELIMINAR y poner en variable de metodo
        filteredRatings = self._filteredRatings

        # creamos objeto data source, para la BDD
        dataSource1 = DataSource()
        adminReview1 = adminReview()
        adminCorrelation1 = adminCorrelation()

        #vaciamos BDD
        adminReview1.deleteAll(dataSource1)
        adminCorrelation1.deleteAll(dataSource1)

        # Guardamos los datos en BDD.Review
        try:
            print('    INICIO TRY')
            # insertamos una por una
            longitud = len(filteredRatings.index)
            print("    longitud del bucle:", longitud)
            print("    INICIO FOR")

            for i in range(0, longitud):
                # GUIA df.values[i][j], j = ...
                # 0:brewery_id 1:brewery_name 2:review_overall 3:review_aroma 4:review_appearance 5:review_profilename
                # 6:beer_style 7:review_palate 8:review_taste 9:beer_name 10:beer_abv 11:beer_beerid
                '''
                print(filteredRatings.index[i], filteredRatings.values[i][11], filteredRatings.values[i][8], \
                      filteredRatings.values[i][7], filteredRatings.values[i][3], filteredRatings.values[i][4], \
                      filteredRatings.values[i][2], filteredRatings.values[i][5])
                '''
                review = \
                    Review(filteredRatings.index[i], filteredRatings.values[i][11], filteredRatings.values[i][8], \
                           filteredRatings.values[i][7], filteredRatings.values[i][3], filteredRatings.values[i][4], \
                           filteredRatings.values[i][2], filteredRatings.values[i][5])

                adminReview1.insertData(dataSource1, review)
            # DESPUES q acaben los inserts hacemos el commit
            print("    FIN FOR")
            dataSource1.commitAction()
            print('    COMMIT DATA OK')
        except Exception as e:
            # si peta se quita to lo que habia antes del ultimo commit
            dataSource1.rollbackAction()
            print(e, '    EXCEPTION!')
        finally:
            # cerramos la conexion con la base
            dataSource1.closeConexion()
            print('    FINALLY OK')

    def crear_corrMatrix(self):
        # Función para crear la matriz de correlación
        '''
        print('LEYENDO JOTASON..')
        # reading the JSON data using json.load()
        file = self._rutaHome+'\\datos\\datosFiltrados.json'
        with open(file) as filtered_file:
            dictFile = json.load(filtered_file)
        # converting json dataset from dictionary to dataframe
        corrMatrix = pd.DataFrame.from_dict(dictFile, orient='index')
        '''
        print("CONSTRUYENDO PIVOT TABLE..")
        beerRatings = self._filteredRatings.pivot_table(index=['review_profilename'], columns=['beer_beerid'],
                                                        values='review_overall')

        # Creamos la matriz de correlación entre cervezas con metodo pearson
        print("CREANDO MATRIZ DE CORRELACION..")
        corrMatrix = beerRatings.corr(method='pearson')  # , min_periods=0)
        print(corrMatrix.head())

        # inicializamos clases para BDD
        print("GUARDANDO ARCHIVOS..")
        dataSource1 = DataSource()
        adminCorr1 = adminCorrelation()

        # inicalizamos parametros para bucle
        i = 0;
        j = 0
        indexes = self._filteredRatings.groupby(["beer_beerid"])["review_overall"].mean()

        # vaciamos tabla
        adminCorr1.deleteAll(dataSource1)

        # bucle para la BDD input

        print('    INICIO BUCLE SAVE CORR MATRIX')
        try:
            for i in indexes.index:
                for j in indexes.index:
                    if i > j:
                        correlation = corrMatrix.loc[i, j]
                        if not math.isnan(correlation):
                            fila = Correlation(i, j, correlation)
                            adminCorr1.insertData(dataSource1,fila)
            # despues q acaben los inserts hacemos el commit
            dataSource1.commitAction()
            print('    FIN FOR CORR MATRIX')
        # se podrian poner distintos tipos de except , pj para saltar si ya esta añadido en vez q pete

        except Exceptiona as e:
            # si peta se quita to lo que habia antes del ultimo commit
            dataSource1.rollbackAction()
            print(e, "    EXCEPT!")
        finally:
            # cerramos la conexion con la base
            dataSource1.closeConexion()
            print('    FINALIZADO')

        # Guardamos la correlacion en un JSON, provisional
        # corrMatrix.to_json(self._rutaHome+'\\datos\\corrMatrix.json',orient='index')

    #Función para obtener ratings por id de cerveza y puntuación
    def setMyRatingByBeerList(self, beerDict):
        self._myRatings = beerDict

    #Funcion que realiza la comprobacion de los filtros deseados
    def comprobacionFiltros(self, style, abv, typeAbv, beer_corr):
        #Iniciamos variables
        comprobacion = True
        abv = abv.split("-")
        #Recogemos los valores de la cerveza
        beer_abv = beer_corr.getAbv()
        beer_style = beer_corr.getStyle()
        #Comprobamos el estilo
        if style != "-1":
            if style.upper().find(beer_style.upper()) == -1:
                comprobacion = False
        #Comprobamos la graduacion
        if comprobacion and abv != "-1" and typeAbv != "-1":
            if (typeAbv == "menor" and float(abv[0]) < beer_abv)\
            or (typeAbv == "mayor" and float(abv[0]) > beer_abv)\
            or (typeAbv == "entre" and (float(abv[1]) > beer_abv or float(abv[0]) < beer_abv)):
                comprobacion = False

        return comprobacion

    #Función genérica para obtener los ratings
    def myRatings(self, style, abv, typeAbv):
        simCandidates = pd.Series()

        #inicializamos clases para BDD y variables
        dataSource1 = DataSource()
        adminCorr1 = adminCorrelation()
        adminBeer1 = adminBeer()
        dictBeers = {}

        #Recorremos la lista de ratings y seleccionamos aquellos con puntuación mayor a 2
        for ratedBeer, puntuacion in self._myRatings.items():

            if float(puntuacion) > 2:
                # Recupera la correlacion de la cerveza puntuada
                correlationsBeers = adminCorr1.getById(dataSource1, int(ratedBeer))
                #Se recoge las "correlaciones"
                for corr in correlationsBeers:
                    #Se comprueba cual de las dos es la diferente a la puntuada
                    beerid_corr = None
                    if int(ratedBeer) != int(corr.getBeer_id()):
                        beerid_corr = corr.getBeer_id()
                    else:
                        beerid_corr = corr.getBeer_idcorr()
                    #Se recoge la cerveza diferente
                    beer_corr = adminBeer1.getById(dataSource1, beerid_corr)
                    #Se comprueba que cumple los filtros

                    if self.comprobacionFiltros(style, abv, typeAbv, beer_corr) and corr.getCorrelation()>0:
                        #Añadimos el elmento al diccionario, y si esta se suma el valor con el que ya habia
                        if beer_corr.getBeer_id() not in dictBeers:
                            dictBeers[beer_corr.getBeer_id()] = float(corr.getCorrelation()) * float(puntuacion)
                        else:
                            dictBeers[beer_corr.getBeer_id()] = float(dictBeers[beer_corr.getBeer_id()]) + float(corr.getCorrelation()) * float(puntuacion) 
        #Ordenamos el diccionario        
        dictBeers = sorted(dictBeers.items(), key=operator.itemgetter(1), reverse=True)
        #Solo devolvemos los diez primeros resultados
        del dictBeers[10:]
        return dictBeers

