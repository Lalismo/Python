'''La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:


* Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.

* Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.

* Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.

* Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.

Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos. 
'''
from random import randint

nombre = input('Cual es tu nombre? ')
intentos = 1
num_Aleatorio = randint(1,100)


print(f'Bien {nombre}  he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número? ')

while intentos <= 8:
    respuesta = int(input(f'Bien {nombre} Cual es el numero?: '))

    if(respuesta < 1 and respuesta > 100):
        print('Tu numero no esta permitido')
    elif(respuesta < num_Aleatorio):
        print('El numero es incorrecto has elegido un numero menor al numero secreto')
    elif(respuesta > num_Aleatorio):
        print('El numero es incorrecto has elegido un numero mayor al numero secreto')
    elif(respuesta == num_Aleatorio):
        print(f'Has ganado! en {intentos} intentos')
        break
    
   
    intentos += 1
    
   
    
