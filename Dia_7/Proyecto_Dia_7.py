'''Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos:
nombre y apellido. Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a
heredar de Persona, porque los clientes son personas, por lo que el Cliente va a heredar
entonces los atributos de Persona, pero también va a tener atributos propios, como número
de cuenta y balance, es decir, el saldo que tiene en su cuenta bancaria.
Pero eso no es todo: Cliente también va a tener tres métodos. El primero va a ser uno de los
métodos especiales y es el que permite que podamos imprimir a nuestro cliente. Este método
va a permitir que cuando el código pida imprimir Cliente, se muestren todos sus datos,
incluyendo el balance de su cuenta. Luego, un método llamado Depositar, que le va a permitir
decidir cuánto dinero quiere agregar a su cuenta. Y finalmente, un tercer método llamado
Retirar, que le permita decidir cuánto dinero quiere sacar de su cuenta.
Una vez que hayas creado estas dos clases, tienes que crear el código para que tu programa se
desarrolle, pidiéndole al usuario que elija si quiere hacer depósitos o retiros. El usuario puede
hacer tantas operaciones como quiera hasta que decida salir del programa. Por lo tanto, nuestro
código tiene que ir llevando la cuenta de cuánto dinero hay en el balance, y debes procurar, por
supuesto, que el cliente nunca pueda retirar más dinero del que posee. Esto no está permitido. 
'''

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido =  apellido
    
class Cliente(Persona):
    
    def __init__(self, nombre, apellido,numero_cuenta,balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido} con numero de cuenta: {self.numero_cuenta} y balance: {self.balance}'
    
    def depositar(self,deposito):
        self.balance += deposito
        print('Deposito realizado correctamente!')
        return self.balance 
    
    def retirar(self,retiro):
        
        if retiro > self.balance:
            print('Su retiro es mayor a su balance.')
        else:
            self.balance -= retiro
            print('Retiro realizado correctamente!')
        return self.balance


 
def crear_cliente():

    nombre = input('Digite el nombre del cliente: ')
    apellido =  input('Digite los apellidos del cliente: ')
    numero_cuenta = input('Digite el numero de cuenta del cliente: ')
    cliente = Cliente(nombre,apellido,numero_cuenta)
    return cliente

def inicio():
    es_valido = False
    opcion = 0
    print('''Bienvenido a tu cuenta bancaria favorita
Para empezar crea tu cuenta bancaria''')
    
    cliente = crear_cliente()

    while not es_valido:
        print('''Bienvenido al menu:
              1. Vicualizar Datos
              2. Depositar
              3. Retirar
              4. Salir''')
        opcion = int(input('Selecciona la opcion que quieres realizar: '))

        match opcion:
            case 1:
                print(cliente)
            case 2:
                deposito = int(input('Digite el monto a depositar: '))
                cliente.depositar(deposito)
            case 3:
                retiro = int(input('Digite cuanto quiere retirar de la cuenta: '))
                cliente.retirar(retiro)
            case 4:
                print('Hasta pronto!')
                break
            case _:
                print('Opcion fuera de rango')            
        
        
inicio()