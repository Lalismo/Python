'''
Práctica Return 3
Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento,
invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras,
para sumisitrarle como argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.
'''
palabra = "Python"
def invertir_palabra(palabra):
    palabra = palabra.upper()
    palabra = palabra[::-1]
    return palabra

resultado = invertir_palabra(palabra)
print(resultado)
