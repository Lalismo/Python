'''
Práctica Métodos de String 3
Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas.
'''

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
palabra1 = frase.replace("difícil", "fácil")
frase_final =palabra1.replace("mala", "buena")
print(frase_final)