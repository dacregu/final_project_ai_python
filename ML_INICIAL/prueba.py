import pandas as pd
from recomendacion_cervezas import *

#cosa = Recomendaciones()
#cosa.leerYfiltrar()


recomendaciones = Recomendaciones()
#recomendaciones.crear_corrMatrix()

beerDict = {}
beerList = "5481|5"
beerList=beerList.split(';')

#Recorre la lista de beers y separbmos id y puntuación, se guarda en diccionario
for beer in beerList:
    splitbeer = beer.split('|')
    beer_id = splitbeer[0]
    puntuacion = splitbeer[1]
    beerDict[beer_id] = puntuacion

recomendaciones.setMyRatingByBeerList(beerDict)


#print(recomendaciones.myRatings( "Baltic Porter", "10-5", "entre"))
print("PRUEBA SIN FILTROS")
#print(recomendaciones.myRatings( "-1", "-1", "-1"))
print("PRUEBA ESTILO")
#print(recomendaciones.myRatings( "Baltic Porter", "-1", "-1"))
print("PRUEBA GRADUACION MAYOR")
#print(recomendaciones.myRatings( "-1", "7", "mayor"))
print("PRUEBA GRADUACION MENOR")
#print(recomendaciones.myRatings( "-1", "7", "menor"))
print("PRUEBA TODOS")
print(recomendaciones.myRatings( "American IPA", "10-5", "entre"))


'''
dataSource = DataSource()

adminBeer = AdminBeer()
#Del csv recoges beer_id, Brewey_id, name, style, abv
try:
	#Esto sera en bucle
	beer = Beer(beer_id, brewery_id, name, style, abv)
	adminBeer.insertData(dataSource, beer)
	#Cuando acaben los inserts hacemos el commit
	dataSource.commitAction()
except:
	dataSource.rollbackAction()
finally:
	dataSource.closeConexion()

'''
