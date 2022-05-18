#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.


frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contador = 0

for i in frase: 
    if i == letra:
        contador += 1

print("La letra %s aparece %2i veces en la frase '%s'." % (letra, contador, frase))   #otra  manera adiconal al .format.. para incluir variables en una cadena.  
                                                                                    # %s para cadenas Y %2i para enteros... % (variables)


