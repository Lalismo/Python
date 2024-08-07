'''
Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente
la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
'''
#Para saber la cantidad de elementos que se tienen en el diccionario de kwargs 
#Solo utilizariamos len ya que kwargs usa el formato de diccionario, en pocas palabras es un diccionario
def cantidad_atributos(**kwargs):
    return len(kwargs)
        
    
print(cantidad_atributos(x=76,y=5,z=2))