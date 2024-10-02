#Importar flask, jsonify, request
from flask import Flask, jsonify, request as req
#import pandas as pd
#Importar clase recomendacion_beer
from recomendacion_cervezas import *
from DataSource import *
from adminBeer import *
from classBeer import *
#Generbr la app de flask
app = Flask(__name__)

#Generbmos el objeto de recomendaciones
recomendaciones = Recomendaciones()

#Ruta parb entrenar el algoritmo
@app.route("/trainRecomendaciones", methods=["POST"])
#Función parb entrenar el algotimo
def trainRecomendaciones():
    recomendaciones.crear_corrMatrix()
    return jsonify({"OK":"OK"})

#Ruta parb recomendar beers por lista de beers y puntuación
@app.route("/recomendacion_beers", methods=["GET"])
#Función parb recomendar beers por lista de beers y puntuación
def recomendarbeers():
    beerList = req.args.get('beers')
    style = req.args.get('style')
    abv = req.args.get('abv')
    typeAbv = req.args.get('typeAbv')
    beerDict = {}
    beerList=beerList.split(';')
    beers = []
    
    #Recorre la lista de beers y separbmos id y puntuación, se guarda en diccionario
    for beer in beerList:
        splitbeer = beer.split('|')
        beer_id = splitbeer[0]
        puntuacion = splitbeer[1]
        beerDict[beer_id] = puntuacion

    recomendaciones.setMyRatingByBeerList(beerDict)
    
    #Crea lista de recomendaciones a partir de diccionario de beers
    rb = recomendaciones.myRatings(style, abv, typeAbv)
    #CODIGO BUENO BONICO
    #return jsonify({"beers": rb})
    #Objeto de la BBDD
    dataSource = DataSource()
    #Objeto que administra la tabla beers
    adminBeer1 = adminBeer() 

    #Crea matriz de titulo y puntuación de las recomendaciones
    for row in rb:
        beer = adminBeer1.getById(dataSource,int(row[0]))
        beers.append({"beer": beer.getName(), "style": beer.getStyle(), "abv": beer.getAbv()})

    #Devuelve jason
    return jsonify({"beers": beers}) 

#Ruta para recoger todas las cervezas
@app.route("/getAll_beers", methods=["GET"])
#Funcion para recoger todas las cervezas
def getAllBeers():
    #Objeto de la BBDD
    dataSource = DataSource()
    #Objeto que administra la tabla beers
    adminBeer1 = adminBeer()
    #Lista donde se almacenaran las cervezas
    lista_beers = []

    #Recogida de todas las cervezas en la BBDD
    beers = adminBeer1.getAll(dataSource)
    #Se recogen las cervezas y se añaden a la lista, solo nombre e id
    for beer in beers:
        lista_beers.append({"beer_name":beer.getName(), "beer_id": beer.getBeer_id()})

    #Se cierra la conexion con la BBDD
    dataSource.closeConexion()
    #Se devuelven las cervezas en formato JSON
    return jsonify({"beers": lista_beers})


#Ruta para recoger todos los estilos
@app.route("/getAll_estilos", methods=["GET"])
#Funcion para recoger todos los estilos
def getAllEstilos():
    #Objeto de la BBDD
    dataSource = DataSource()
    #Objeto que administra la tabla beers
    adminBeer1 = adminBeer()
    #Lista donde se almacenaran los estilos
    lista_styles = []

    #Recogida de todas los "estilos" en la BBDD
    beers = adminBeer1.getEstilos(dataSource)
    #Se recogen las cervezas y se añaden a la lista, solo el estimo
    for beer in beers:
        lista_styles.append({"estilo": beer.getStyle()})

    #Se cierra la conexion con la BBDD
    dataSource.closeConexion()
    #Se devuelven los estilos en formato JSON
    return jsonify({"estilos": lista_styles})
