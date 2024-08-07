from collections import Counter, defaultdict, namedtuple

#Saber cuantas veces aparece un numero utilizando diccionarios y Counter
numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]
print(Counter(numeros))
print('----------')

#Contar cuantas veces aparece una palabra en una frase
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))
print('----------')

#Encontrar el mas repetido con most_common
serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,4])
print(serie.most_common())
print('----------')
print(list(serie))
print('----------')

#Utizando el metodo defaultdict
mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print('----------')

print(mi_dic)
print('----------')

#Utilizando el metodo namedtuple
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.45, 86)
print(ariel)
print('----------')

print(ariel.altura)
print('----------')

print(ariel[2])