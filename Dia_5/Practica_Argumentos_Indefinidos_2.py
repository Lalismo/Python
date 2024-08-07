'''Práctica sobre Argumentos Indefinidos (*args) 2
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos 
(es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).'''

def suma_absolutos(*args):
    num = 0
    absoluto = -2
    suma = 0
    resta = 0
    for arg in args:
        if arg < num:
            num = arg * absoluto # 0 = -7 * -2
            resta = num + arg
            suma +=resta
        else:
            suma += arg

    return suma
            
print(suma_absolutos(-7,-7))        
            
            