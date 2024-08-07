'''Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
estas opciones que tenemos aquí:

1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.

2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.

3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.

4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar.

5. La opción 5, le va a preguntar qué categoría quiere eliminar.

6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código. 
'''
from pathlib import Path
import os

path_Receta = Path(Path.home(),'Recetas')

def leer_receta():
    respuesta = False
    while not respuesta:
        lista_Recetas = []
        for txt in  Path(path_Receta).glob('*'):
            lista_Recetas.append(txt.name)

        print('Las categorias son: ')

        for mostrar_Categoria in set(lista_Recetas):
            print(mostrar_Categoria)

        categoria = input('Elige una categoria: ')
        mostrar_Recetas = Path(path_Receta,categoria)
        
    
        for txt in  Path(mostrar_Recetas).glob('*.txt'):
            print(txt.stem)
      
        
        if Path(mostrar_Recetas,txt).is_file():
            receta = input('Que receta quiere leer? ')
            leer_receta = Path(mostrar_Recetas,receta+'.txt')
            print(leer_receta.read_text())
        else:
            print('No hay recetas creadas en esta categoria.')
        

        pregunta = input('Desea continuar? s/n: ')
        if pregunta == 's':
            respuesta = False
            os.system('cls')
        elif pregunta == 'n':
            respuesta = True
            os.system('cls')

    
def crear_receta():
    respuesta = False
    lista_recetas = []
    while not respuesta:
        for txt in  Path(path_Receta).glob('*'):
            lista_recetas.append(txt.name)
        print('Las categorias son: ')

        for mostrar_Categoria in set(lista_recetas):
            print(mostrar_Categoria)

        categoria = input('Elige una categoria: ')
        nombre_Archivo = input('Elige el nombre de la receta: ')
        contenido_Receta = input('Introduce el contenido de la receta: ')
        nuevo_archivo = Path(path_Receta,categoria,nombre_Archivo+'.txt')
        nuevo_archivo.open('w')
        nuevo_archivo.write_text(contenido_Receta)
        print(f'Receta {nuevo_archivo.name} creada correctamente')
        pregunta = input('Desea continuar? s/n: ')
        if pregunta == 's':
            respuesta = False
            os.system('cls')
        elif pregunta == 'n':
            respuesta = True
            os.system('cls')
     
    
def crear_categoria():
    respuesta = False
    while not respuesta:
        categoria = input('Escoge el nombre de la categoria de resetas: ')
        path_categoria = Path(path_Receta,categoria)
        path_categoria.mkdir()
        print(f'Carpeta {path_categoria.name} creada correctamente')
        pregunta = input('Desea continuar? s/n: ')
        if pregunta == 's':
            respuesta = False
            os.system('cls')
        elif( pregunta == 'n'):
            respuesta = True
            os.system('cls')
    
    
def eliminar_receta():
    lista_recetas = []
    for txt in  Path(path_Receta).glob('*'):
        lista_recetas.append(txt.name)
    print('Las categorias son: ')

    for mostrar_Categoria in set(lista_recetas):
        print(mostrar_Categoria)
    
    categoria = input('Elige una categoria: ')
    mostrar_Recetas = Path(path_Receta,categoria)

    for txt in  Path(mostrar_Recetas).glob('*.txt'):
        print(txt.stem)
    
    receta = input('Que receta quiere leer? ')
    eliminar_receta = Path(mostrar_Recetas,receta+'.txt')
    os.remove(eliminar_receta)
    print('Receta eliminada correctamente')
    
def eliminar_categoria():
    lista_recetas = []
    for txt in  Path(path_Receta).glob('*'):
        lista_recetas.append(txt.name)
    print('Las categorias son: ')

    for mostrar_Categoria in set(lista_recetas):
        print(mostrar_Categoria)
    
    categoria = input('Escoge la categoria a eliminar: ')
    eliminar_categoria = Path(path_Receta,categoria)
    for txt in os.listdir(eliminar_categoria):
        os.remove(Path(eliminar_categoria,txt))
    eliminar_categoria.rmdir()
    print('Categoria eliminada correctamente')

    
    
def finalizar_programa():
    print('Hasta pronto!')



def menu():
    indice = 0
    for txt in  Path(path_Receta).glob('**/*.txt'):
        if txt.exists():
            indice +=1
    print(f'Las recetas se encuentran en: {path_Receta}')
    print(f'Total de recetas: {indice}')
 
    es_valido = False
    opcion = 0
   
    while not es_valido:
        print('''Selecciona la opción que quieres realizar
            1. leer recetas
            2. crear recetas
            3. crear categorias
            4. eliminar receta
            5. eliminar categoria
            6. finalizar programa 
        ''')
        opcion = int(input('selecciona una respuesta: '))
        
        match opcion:
            case 1:
                leer_receta()
                
            case 2:
                crear_receta()
            case 3:
                crear_categoria()
            case 4:
                eliminar_receta()
            case 5:
                eliminar_categoria()
            case 6:
                return finalizar_programa()
            case _:
                print('Numero fuera de rango')
  
menu()

