'''
Escribe una función que requiera una cantidad indefinida de argumentos.
Lo que hará esta función es devolver True si en algún momento se ha ingresado
al numero cero repetido dos veces consecutivas.

Por ejemplo:
(5,6,1,0,0,9,3,5) -> True
(6,0,5,1,0,3,0,1) -> False
'''
#Primer solución que encontre utilizando listas
def numeros(*args):
    
    Primer_0 = args.index(0)
    Segundo_0 = Primer_0 + 1
    lista = []
    for arg in args:
        lista.append(arg)


    if lista[Primer_0] == 0 and lista[Segundo_0] == 0:
        
        return True
    else: 
        return False

print(numeros(5,6,1,0,0,9,3,5))

#Solución utilizando tupla

def numeros(*args):
    
    Primer_0 = args.index(0)
    Segundo_0 = Primer_0 + 1
    
  
    if args[Primer_0] == 0 and args[Segundo_0] == 0:
        
        return True
    else: 
        return False

print(numeros(0,5,6,1,0,0,9,1,1,0))
