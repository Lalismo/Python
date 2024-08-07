class Pajaro:
    #Atributos de clases
    
    alas = True

    #Constructor de la clase
    def __init__(self,color, especie):
        self.color = color
        self.especie = especie
    #Metodos de instancia, acceder y modificar atributos del objeto, acceder a otros metodos y modificar el estado de la clase
    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()
    
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    #Metodos de clase
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    #Metodos estaticos
    #Estos metodos no se pueden relacionar con los demas metodos
    @staticmethod
    def mirar():
        print('El pajaro mira')



#Instancias de metodos de instancia
piolin =Pajaro('amarillo','canario')
piolin.pintar_negro()
piolin.volar(50)
piolin.alas = False
print(piolin.alas)
print('-----------')

#Instancias de metodos de clase
Pajaro.poner_huevos(3)
print('-----------')

#Instancias de metodos estaticos
Pajaro.mirar()

    