'''
Imagina esta situación: tu mejor amigo ha puesto una fábrica de cerveza y tiene todo listo.
Su producto es fantástico, tiene cuerpo, buen sabor, buen color, el nivel justo de espuma…
pero le falta una identidad. No se le ocurre qué nombre ponerle su cerveza para que
tenga una identidad única y original. Entonces vienes tú y le dices 
"No te preocupes, yo voy a crear un programa que te va a hacer dos preguntas y
luego te va a decir cuál es el nombre de tu cerveza". Así de simple.
Ya sé que en el mundo real no necesitaríamos desarrollar un software solo para hacer dos
preguntas, pero hasta que aprendamos más funcionalidades los programas van a tener que
mantenerse en el terreno de lo simple. Igualmente, si está recién comenzando, este va a ser
todo un desafío.
Vas a crear un código en Python que le pida a tu amigo que responda dos preguntas que
requieran una sola palabra cada una y que luego le muestre en pantalla esas palabras
combinadas, para formar una marca creativa.
Puedes usar las preguntas que quieras. La idea es que el resultado sea original, creativo, y hasta
cómico, y si quieres agregar dificultad al desafío, te sugiero que intentes que el nombre de la
cerveza se imprima entre comillas. Recuerda que hay diferentes formas de que la función print
muestre las comillas sin cortar el string, y que ingrese la impresión final en al menos dos líneas
utilizando saltos de línea dentro del código. 
'''
pregunta1= input("¿Cual es el nombre de tu perro?")
pregunta2= input("¿Cual es tu juego favorito?")

print(f'El nombre de tu cerveza es: "{pregunta1} {pregunta2}" ')