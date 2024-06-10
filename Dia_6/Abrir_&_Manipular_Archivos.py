#Para poder obtener nuestro archivo que queremos leer se necesita de su ubicacion
mi_archivo = open('Dia_6\prueba.txt')
#Una vex obtenido, podemos leerlo y mostrarlo en pantalla con print
print(mi_archivo.read())
#Siempre es recomendado cerrar nuestro archivo para que no consuma cada vez mas memoria
mi_archivo.close()

print('---------')
#Para leer y mostrar solo una linea
Una_linea = open('Dia_6\prueba.txt')
#Se mostrara la primer linea, al finalizar cada linea, tiene un salto de linea
#Si se quiere quitar ese salto de linea y no dejar espacios, con el metodo rstrip() al final de cada
print(Una_linea.readline().rstrip())
#Pero si agregamos otra nueva función, se muestra la siguente
print(Una_linea.readline().rstrip())
#Y la siguiente, hasta mostrar las 3 lineas
print(Una_linea.readline())
Una_linea.close()

print('---------')

#Tambien podemos iterar linea por linea
iterarlinea = open('Dia_6\prueba.txt')
for linea in iterarlinea:
    print(f'Aqui dice: {linea.rstrip()}')
iterarlinea.close()

#Almacenamiento del contenido de un archivo en una lista

print('---------')

listalinea = open('Dia_6\prueba.txt')

listaDeLineas = listalinea.readlines()
print(listaDeLineas)
listaDeLineas.close()