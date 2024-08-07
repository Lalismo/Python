'''
Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona,
que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
'''

def describir_persona(nombre,**kwargs):
    nombre_argumento = ''
    valor_argumento = ''
    print(f'Caracteristicas de {nombre}:')
    for clave, valor in kwargs.items():
        nombre_argumento = clave
        valor_argumento = valor
        print(f'{nombre_argumento}: {valor_argumento}')
        

print(describir_persona("María", color_ojos="azules", color_pelo="rubio"))
