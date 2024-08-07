class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f'{self.nombre} dice muu')

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f'{self.nombre} dice bee')

vaca1 = Vaca('Lola')
obeja1 = Oveja('Lala')


#El polimorfismo nos sirve en hacer llamar algun metodo de una forma mas sencilla si se tienen 
#Varias instancias que comparten ese mismo metodo o al crear funciones que ejecuten ese metodo
#Sin importar que tipo de objeto se pase
animales = [vaca1,obeja1]
for animal in animales:
    animal.hablar()