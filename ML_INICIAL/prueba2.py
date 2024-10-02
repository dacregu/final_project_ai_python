import pandas as pd
import numpy as np
from recomendacion_cervezas import *
import sys
sys.path.insert(1, './BBDD/whatthebeer')
from DataSource import *



cosa = Recomendaciones()
print('+ LEER Y FILTRAR')
cosa.leerYfiltrar(100000)
cosa.paBeers()
## hay que modificar la funcion de arriba y poner un return para que quede:
## cosa.guardarFiltrado(cosa.leerYfiltrar())
print('\n+ GUARDAR FILTRADO')
cosa.guardarFiltrado()
print('\n+ CREAR CORR MATRIX')
cosa.crear_corrMatrix()

