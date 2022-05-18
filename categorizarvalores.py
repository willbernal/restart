
#Con Python, puede mezclar tipos en una lista. En este laboratorio, creará una lista con diferentes tipos e imprimirá los valores.

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

#ciclo for.. para cada item(variable), dentro de mi lista, y dos puntos: (abrir el bloque de codigo)
# todo lo que este con separacion es un dato.  
# for tiene limite. 
# por cada posicion que vaya recorriendo, le asigna el valor a la variable. en el caso es item. 
# el print esta formateado. puedo usar diferentes variables que se las puedo asignar a cada conjunto de llaves, las cuales toman el primer valor del formateo..  .format
# 

