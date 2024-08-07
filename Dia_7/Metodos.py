class Pajaro:
    #Atributos de clases
    
    alas = True

    #Constructor de la clase
    def __init__(self,color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')

piolin =  Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(50)