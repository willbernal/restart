


#estructura de datos que continen una coleccion o secuiencia de datos separados por un delimitador. 

#listas: siempre con llaves cuadradas, 

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[2])

myFruitList[2] = "orange"

print(myFruitList)

#tuplas: siempre con parentesis, la tupla NO es modificable.  (inmutable)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


#Diccionario: es una lista de parejas de elementos que tiene nombres asignados o claves que no se pueden repetir.  {}     las claves NO se pueden modificar.  estan separados por: 
#ejemplo capitales = {'Chile':'Santiago', 'España':'Madrid', 'Francia':'París'}

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)

print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])

print(myFavoriteFruitDictionary["Paulo"])

#adicionar al diccionario: 
myFavoriteFruitDictionary ['Amenabar'] = 'Cineasta'

print(myFavoriteFruitDictionary["Amenabar"])

print(myFavoriteFruitDictionary)

#eliminar del diccionario
del myFavoriteFruitDictionary ["Amenabar"]

print(myFavoriteFruitDictionary)
