class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self): 
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')
    
    def volar(self, metros):
        print(f'el pajaro vuela {metros} metros')

class Pajaro(Animal):
#Agregar atributos de clase heredada
    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo =  altura_vuelo


    def hablar(self):
        print('pio')




piolin = Pajaro(2,'amarillo',12)
#Metodo heredado sin cambios
piolin.nacer()
print('-------------')

#Metodo heredado y modificado
piolin.hablar()
print('-------------')

#Metodos nuevos sin heredar
piolin.volar(100)

print('-------------')


#Para saber de quien hereda
print(Pajaro.__base__)
print('-------------')

#Para saber a quien le da herencia
print(Animal.__subclasses__())