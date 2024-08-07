class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo =  titulo
        self.canciones = canciones

    #Para devolver en un formato determinado para la forma base de nuestra clase
    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'
    
    #Definir el largo de nuestra clase
    def __len__(self):
        return self.canciones
    
    #Agregar mensajes o nuevas funciones con los metodos especiales
    def __del__(self):
        print('Se ha eliminado el CD')

mi_cd = CD('Pink Floyd', 'The Wall', 24)
print(mi_cd)

print(len(mi_cd))

del mi_cd
        