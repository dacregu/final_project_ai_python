from adminBeer import *
from DataSource import *

beer1 = Beer(1,2,"Moritz Epidor", "IPA",5.5)
beer2 = Beer(3,1,"Estrella Galicia","Pilsen",4.5)
dataSource = DataSource()
consulta = adminBeer()

'''beers = consulta.getAll(dataSource)
consulta.closeConexion()

for beer in beers:
    print(beer.getName())


beers = consulta.getEstilos(dataSource)

for beer in beers:
    print(beer.getStyle())



beer = consulta.getById(dataSource,2)

print(beer.getBeer_id()," ",beer.getName())'''


'''fallo=consulta.insertData(dataSource,beer2)
print(fallo)
dataSource.commitAction()
dataSource.closeConexion()'''

'''consulta.updateData(dataSource, beer1)
dataSource.commitAction()
dataSource.closeConexion()'''

consulta.deleteData(dataSource,beer2)
dataSource.commitAction()
dataSource.closeConexion()
