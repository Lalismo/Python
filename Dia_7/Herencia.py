class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self): 

        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

piolin = Pajaro(2,'amarillo')
piolin.nacer()
print('-------------')


#Para saber de quien hereda
print(Pajaro.__base__)
print('-------------')

#Para saber a quien le da herencia
print(Animal.__subclasses__())



