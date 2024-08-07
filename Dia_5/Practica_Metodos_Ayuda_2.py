'''
Práctica Métodos y Ayuda 2
Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando

el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.
'''

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
print(frutas)
#La función insert hace que proporcionemos el indice y el nombre del elemento que queremos insertar
frutas.insert(3,'naranja')

print(frutas)