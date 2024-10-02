import requests as req

opcion = -1

print("Antes de todo una pequeña explicacion: "\
	+"-----Esto es un producto minimo y no se asemeja al producto final----"\
	+"\nNuestro programa se basa en un recomendador de cervezas, aqui tenemos for defecto que te recomienda en base a la cerveza 'Galicia' con una puntuacion de 5."\
	+"\nLuego tenemos una serie de filtros en base a un estilo y/o la graduacion.")
input("\nIntro para continuar")	
while(opcion!="0"):
	print("=============== RECOMENDADOR beers ===============")
	opcion = input("Elige una opcion:\n1. Recomendaciones Cerveza Estrella Galicia"\
					+"\n2. Recomendaciones Cerveza Estrella Galicia con estilo 'American Adjunct Lager'"\
					+"\n3. Recomendaciones Cerveza Estrella Galicia con estilo graduacion mayor que 7"\
					+"\n4. Recomendaciones Cerveza Estrella Galicia con estilo graduacion menor que 7"\
					+"\n5. Recomendaciones Cerveza Estrella Galicia con estilo graduacion entre 10 y 5"\
					+"\n0. Salir\n\n")


	if opcion == "1":
		#url = "http://dqueralt.pythonanywhere.com/recomendacion_beers?beers="
		url = "http://localhost:5000/recomendacion_beers?beers=5481|5&style=-1&typeAbv=-1&abv=-1"
		print("Cargando datos...")
		res = req.get(url)
		data = res.json()
		print(data)
		input("\nIntro para salir")		
	elif opcion == "2":
		#url = "http://dqueralt.pythonanywhere.com/recomendacion_beers?beers="
		url = "http://localhost:5000/recomendacion_beers?beers=5481|5&style=American Adjunct Lager&typeAbv=-1&abv=-1"
		print("Cargando datos...")
		res = req.get(url)
		data = res.json()
		print(data)
		input("\nIntro para salir")	
	elif opcion == "3":
		#url = "http://dqueralt.pythonanywhere.com/recomendacion_beers?beers="
		url = "http://localhost:5000/recomendacion_beers?beers=5481|5&style=-1&typeAbv=mayor&abv=7"
		print("Cargando datos...")
		res = req.get(url)
		data = res.json()
		print(data)
		input("\nIntro para salir")	
	elif opcion == "4":
		#url = "http://dqueralt.pythonanywhere.com/recomendacion_beers?beers="
		url = "http://localhost:5000/recomendacion_beers?beers=5481|5&style=-1&typeAbv=menor&abv=7"
		print("Cargando datos...")
		res = req.get(url)
		data = res.json()
		print(data)
		input("\nIntro para salir")	
	elif opcion == "5":
		#url = "http://dqueralt.pythonanywhere.com/recomendacion_beers?beers="
		url = "http://localhost:5000/recomendacion_beers?beers=5481|5&style=-1&typeAbv=entre&abv=10-5"
		print("Cargando datos...")
		res = req.get(url)
		data = res.json()
		print(data)	
		input("\nIntro para salir")
	elif opcion == "0":
		print("Saliendo....")
	else:
		print("Opción no válida")