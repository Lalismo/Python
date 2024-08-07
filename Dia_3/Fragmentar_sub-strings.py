#Ahora en vez de solo extraer 1 solo caracter,
#Podemos hacerlo extrayendo una columna de caracteres
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)
print('.....')

#Para mostrar desde un determinado inicio
#hasta el final de nuestra cadena se puede hacer lo siguiente
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:]
print(fragmento)
print('.....')

#De igual forma se puede hacer al reves
texto = "ABCDEFGHIJKLM"
fragmento = texto[:5]
print(fragmento)
print('.....')

#Si queremos mostrar caracteres con saltos
#Se puede hacer lo siguiente
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)
print('.....')

#Tambien podemos voltear la cadena
texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1]
print(fragmento)
print('.....')
#De igual forma saltearla al reves
texto = "ABCDEFGHIJKLM"
fragmento = texto[::-2]
print(fragmento)
