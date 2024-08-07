'''
Crear un programa que le pida al usuario que ingrese un texto.
El programa le pedira al usuario que tambien ingrese 3 letras
a su eleccion y a partir de ese momento nuestroc+odigo va a procesar
la siguiente información:

1. ¿Cuantas veces aparece cada una de las letras que eligió?

2. Decir al usuario cuántas palabras hay a lo largo de todo el texto.

3. Informar cual es la prmera letra del texto y cual es la ultima

4. El sistema nos va a mostrar como quedaria el texto si invirtieramos el orden de las palabras.

5. El sistema nos va a decir si la palabra "Python" se encuentra dentro del texto
'''

texto = input('Escribe tu texto: ')
letras = input ('Escoge tus 3 letras: ')

#1. ¿Cuantas veces aparece cada una de las letras que eligió?
textoMinus= texto.lower()
letrasMinus=letras.lower()

listaLetras = list(letrasMinus)
contarLetra1 = textoMinus.count(listaLetras[0])
contarLetra2 = textoMinus.count(listaLetras[1])
contarLetra3 = textoMinus.count(listaLetras[2])

#2. Decir al usuario cuántas palabras hay a lo largo de todo el texto.
separarTexto = textoMinus.split()
contarPalabras= len(separarTexto)

RespuestaPython = "Python" in textoMinus


print(f'''
¿Cuantas veces aparece cada una de las letras que eligió?
Las apariciones de la letra {listaLetras[0]} son de: {contarLetra1}
Las apariciones de la letra {listaLetras[1]} son de: {contarLetra2}
Las apariciones de la letra {listaLetras[2]} son de: {contarLetra3}

¿Cuantas palabras hay en el texto?
En el esto hay {contarPalabras} palabras

¿Cual es la primer y ultima letra del texto?
La primer letra del esto es {textoMinus[0]} y la ultima letra es {textoMinus[-1]}

¿Como se veria el texto invertido?
El texto invertido seria: {textoMinus[::-1]}

¿La palabra Python se encuentra dentro del texto?
{RespuestaPython}


''')

