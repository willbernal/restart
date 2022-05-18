# import para importar librerias de funciones, en python o en todos.podemos tener librerias con diferentes funciones. por ejemplo.. lower, upper.. pueden estar empaquetadas 
# en una libreria y para eso usamos el import. ... importar todas las funciones de una libreria a mi programa. 

# vamos a usar if y else, para preguntar si se cumple una condicion.. ejemplo.. si se cumple, entonces haga algo.. si no uso else y hago otra cosa.  o puedo usar elif para 
# un if con otro if... 

# 

#importar librerias   contiene instrucciones para leer archivos csv,, copy tiene instrucciones para trabajar los comandos copy. 
import csv
import copy

#definir la estructura del diccionario.   diferentes etiquetas y valores.   para leer todos los datos que necesito. 
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#usar for para recorrer las llaves del diccionario.  ,, para cada llave valor, en mivehiculo, imprima llave valor.  
for key, value in myVehicle.items():                          #la funcion item es propia del tipo de dato diccionario. va a recorre cada uno de los items
    print("{} : {}".format(key,value))

#definir una lista vacia para almacenar los datos del inventario. 
myInventoryList = []

#genera un apuntardor a la memoria en donde esta el diccionario... (abrir el archivo )

with open('car_fleet.csv') as csvFile:                  #with open,, se usa exclusivamente para manejo de archivos. 
    csvReader = csv.reader(csvFile, delimiter=',')      #csv.reader funcion de la libreria csv             lee el archivo y se lo asigna a csvreader. 
    lineCount = 0                                       #asigna el valor cero a la variable linecount 
    for row in csvReader:                               #para cada fila en csvreader
        #print (row)                        
        if lineCount == 0:                              # si la linea es 0 imprima 
            print(f'Column names are: {", ".join(row)}')   #usa la funcion join para poner separado por coma, cada valor de row
            lineCount += 1                                  #aumenta el contador en 1
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}') 
                                                        #imprimo una lista que estoy manejando una a una .. 
                                                        #para dar formato se puede usar comillas simples y se escriben los valores dentro de las llaves.  
            currentVehicle = copy.deepcopy(myVehicle)   #hace una copia superfcial de myvehiculo, para alimentar los datos.  (apuntador en memoria)
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)        #coloco aca la informacion (lo guarda en la lista)
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

#append .. para ir agregando al final de la lista
# currentVehicle = copy.deepcopy(myVehicle)


#for anidado.. for dentro de for

for myCarProperties in myInventoryList:                 #para las propiedades guardadas en mi lista. haga
    for key, value in myCarProperties.items():           #y para cada key value en propiedades
        print("{} : {}".format(key,value))               #imprima llave valor.
        print("-----")



#se puede hacer un programa en python,. para que lea un archivo de logs. para que busque el mensaje ERROR, lo cargue en una lista y lo almacene. 


