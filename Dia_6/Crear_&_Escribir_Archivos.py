'''
Existen diferentes modos en los que puedes abrir un archivo
El primero es con r que quiere decir read -> leer, 
este solo nos permitira leer el contenido alojado dentro del archivo

w que quiere decir write -> escribir, si el documento esta vacio empezara a escribir
el contenido, pero si ya hay contenido dentro del archivo lo que hara sera reescribirlo
y si el archivo no se ha creado, al momento de ejecutarlo este se crea y si el archivo creado 
requiere de saltos de linea se tienen que poner de manera manual, ya que este modo 
no lo hace por defecto

a es lo mismo que w, solo que si ya tiene contenido el archivo este no lo reescribe,
si no que lo pone al final del archivo
'''

#crear y escribir un nuevo archivo
archivo = open('Dia_6\prueba.txt','w')
archivo.write('Soy el nuevo texto')
archivo.close()

#reescribiendo archivo y con varias lineas con salto de linea
archivo = open('Dia_6\prueba1.txt','w')
archivo.write('Hola\n')
archivo.write('Mundo\n')
archivo.close()

archivo = open('Dia_6\prueba2.txt','w')
archivo.write('''Hola
Mundo
Como
Estan''')
archivo.close()

#Metodo writelines

archivo = archivo = open('Dia_6\prueba.txt','w')
lista = ['Juan','Pedro','Rodrigo','Alberto']

for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

#Modo a para agregar contenido al final de un archivo

archivo = open('Dia_6\prueba.txt', 'a')
archivo.write('Son mis amigos')
archivo.close()