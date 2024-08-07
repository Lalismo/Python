'''
Práctica Path 3
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py"
a partir de la siguiente estructura de carpetas:


Almacena el directorio obtenido en la variable ruta. No olvides importar Path,
y de concatenar el objeto Path que refiere a la carpeta base del usuario.
'''

from pathlib import Path
base = Path.home()
ruta = Path(base,"Curso Python","Día 6","practicas_path.py")