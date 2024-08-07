import bs4
import requests

#Primero hacemos una variable que aloje el link de nuestra pagina
resultado =  requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

#Despues en unavariable utilizamos la libreria bs4 para poder obtener el html de la pagina en un string
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#Utilizamos la variable con la libreria bs4 para obtener elementos por etiqueta de nuestra pagina
# #al utilizar indice si hay mas de 1 busqueda sirve para mostrar solo que que queremos
# # getText() Sirve para mostrar solo el texto sin la etiqueta 
titulo = sopa.select('title')[0].getText()
print(titulo)
print('----------')

#Extraer elementos de una clase e iterarlos
columna_lateral= sopa.select('.sidebar-container .snippet-item')
for p in columna_lateral:
    print(p.getText())

print('----------')

#Extrer imagenes y descargarlas
resultado = requests.get('https://www.escueladirecta.com')
sopa =  bs4.BeautifulSoup(resultado.text, 'lxml')

#Haciendo busqueda de imagenes por clase con solo mostrando el link de la imagen
imagenes =  sopa.select('img')
num = 0

#Al encontrar los elementos de tipo imagen hacemos un loop para nombrar a cada imagen 
# Y poder descargarla
for img in imagenes:
    num +=1
    name = f'imagen_Dia_11_{num}.jpg'
    # Hacemos la busqueda por src que es el link de la imagen
    binary_img = requests.get(img['src'])
    # Pasamos la variable creada para el link a tipo content que esta en bytes
    binary_content = binary_img.content
    # Abrimos un archivo de tipo binario para alojar el contenido de la imagen y el nombre que tendra cada una de ellas
    f = open(name, 'wb')
    # Escribimos el contenido dentro de la imagen
    f.write(binary_content)
    # Cerramos nuestro archivo
    f.close