import shutil, zipfile

# # Para comprimir un archivo con zipfile
# mi_zip =  zipfile.ZipFile('archivo_comprimido.zip', 'w')
# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')

# mi_zip.close()

# # Para descomprimir el contenido de un zip con zipfile

# descomprimir = zipfile.ZipFile('archivo_comprimido.zip', 'r')
# descomprimir.extractall()


# #Comprimir utilizando shutil
# carpeta_origen = 'ruta de la carpeta a comprimir'

# nombre_archivo = 'nombre de como se llamara el .zip'

# shutil.make_archive(nombre_archivo, 'zip', carpeta_origen)

#descomprimir utilizando shutil
shutil.unpack_archive('C:\\Users\\PC\\Downloads\\Proyecto.zip', 'Proyecto_Dia_9', 'zip')