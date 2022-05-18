

lista_asginaturas = []
lista_notas = []

cantidad = int(input("Ingrese el numero de asignaturas a registrar: "))

for numero in range(cantidad):
    lista_asginaturas.append(input("Ingrese la asignatura que estudio: "))
    lista_notas.append(input("Ingrese la nota que saco: "))

for item in zip (lista_asginaturas, lista_notas):                       #la funcion zip me permite agrupar dos listas y generar una tupla.
    print ("estudie", item[0], "y mi nota fue: ", item[1])


# ejemplo de funcion zip

# paises = ["China", "India", "Estados Unidos", "Indonesia"]
# poblaciones = [1391, 1364, 327, 264]
# list(zip(paises, poblaciones))
# [('China', 1391), ('India', 1364), ('Estados Unidos', 327), ('Indonesia', 264)]

#>>> for pais, poblacion in zip(paises, poblaciones):
#     print("{}: {} millones de habitantes.".format(pais, poblacion))

#China: 1391 millones de habitantes.
#India: 1364 millones de habitantes.
#Estados Unidos: 327 millones de habitantes.
#Indonesia: 264 millones de habitantes.
