print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random

number = random.randint(1,10)                                    #random.randint()  permite generar un numero aleatorio en un rango que le digamos.

#print (number)
isGuessRight = False                                               #flag o bandera, se inicializa en el valor, y dentro de la logica se modifica cuando cumpla la condicion. 

while isGuessRight != True:                  # !=  desigualdad        #es un ciclo que permite ejecutar el codigo hasta que se cumpla la condicion. 
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess)) 
        isGuessRight = True                                             #aqui se cambia la bandera a True. y cambia la condicion. 
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


    #pseudocodigo.. escribir en modo humano la ejecucion del bucle.  (frases de lo que debe realizar el codigo) 


#ejercicio de for en un rango de 0 a 10

print("Count to 10!")

for x in range (0, 11):
    print(x)



