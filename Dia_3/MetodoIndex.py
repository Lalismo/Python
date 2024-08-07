
#Para imprimir la primera letra
texto = "Esta es una prueba"
resultado = texto[0]
print(resultado)
print('.....')
#El signo - se utiliza para traer una letra de texto, 
#pero de forma iniciando desde la parte de atras

texto = "Esta es una prueba"
resultado = texto[-4]
print(resultado)
print('.....')

#El metodo index utiliza para encontrar el indice de una letra o palabra,
#Que se encuentre dentro de la cadena de texto, al no estar se generaria una excepción
texto = "Esta es una prueba"
resultado = texto.index("n")
print(f'La letra n se encuentra en la posición: {resultado}')
print('.....')

texto = "Esta es una prueba"
resultado = texto.index("prueba")
print(f'La palabra prueba inicia desde la posición: {resultado}')
print('.....')

#Si se quiere allar una letra/palabra repetida varias veces,
#Solo mostrara la primer posición de esta letra
texto = "Esta es una prueba"
resultado = texto.index("a")
print(f'La primer posición de la letra a es: {resultado}')
print('.....')

#Ahora si queremos encontrar la segunda posición de la letra a
#Podemos agregar otro parametro dentro del metodo index,
#El cual es star y nosotros indicaremos desde que posicion queremos que empiece a buscar
texto = "Esta es una prueba"
resultado = texto.index("a",5)
print(f'La segunda posición de la letra a es: {resultado}')
print('.....')

#Existe otro metodo el cual es rindex,
#El cual la busqueda que hace es de derecha a izquierda
texto = "Esta es una prueba"
resultado = texto.rindex("a")
print(f'La ultima posición de la letra a es: {resultado}')