'''
Práctica Return 1
Crea una función llamada potencia que tome dos valores numéricos como argumentos.
Deberá devolver el número que resulte de resolver una potencia,
utilizando el primer número como base, y el segundo como exponente:
'''

def potencia(base,exponente):
    resultado = base**exponente
    return resultado

resultado = potencia(3,4)

print(resultado)
