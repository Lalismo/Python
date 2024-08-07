import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Funcion para escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    # Almacenar recognizer en variable
    r =  sr.Recognizer()

    #Configurar el microfono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzo la grabacion
        print('ya puedes hablar')

        # Guardar lo que escuhe como audio
        audio =  r.listen(origen)

    try:
        # Buscar en google
        busqueda = r.recognize_google(audio, language='ES-MX')

        # Prueba de ingreso
        print('Dijiste: '+ busqueda)

        # Devolver busqueda
        return busqueda
        
    #´En caso de no comprender el audio
    except sr.UnknownValueError:

        # Prueba de no comprender el audio
        print('No se entendio')

        #Devolver error
        return 'Sigo esperando'
        
        #En caso de no resolver la busqueda
    except sr.RequestError:
            
        # Prueba de no resolvio la busqueda
        print('No se resolvio la busqueda')

        #Devolver error
        return 'Sigo esperando'
        
        # Error inesperado
    except Exception as e:

        # Prueba de error inesperado
        print(e)

        #Devolver error
        return 'Sigo esperando'

#  Funcion para que el asistente pueda ser escuchado              
def hablar(mensaje):
    #Endender a pyttsx3
    engine =  pyttsx3.init()

    #Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Fincoon para informar el dia de la semana
def pedir_dia():
    #Crear variable con datos de hoy
    fecha =  datetime.date.today()
    print(fecha)

    #crear variable para el dia de la semana
    dia_semana =  fecha.weekday()
    print(dia_semana)

    #Diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    
    # Decir dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

# Funcion para informar hora
def pedir_hora():
    # Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora =  f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # Decir la hora
    hablar(hora)

# Funcion saludo inicial
def saludo_inicial():

    # Variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour <13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'


    #decir el saludo
    hablar(f'{momento}, soy tu asistente personal. que es lo que necesitas terrunzito de azucar')

#Funcion central del asistente
def pedir():

    #Activar saludo inicial
    saludo_inicial()

    #Variable de corte
    comenzar =  True
    while comenzar:
        #Activar el micro y guardar el pedido en un string
        pedido =  transformar_audio_en_texto().lower()

        if 'abras youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abras navegador' in pedido:
            hablar('Claro espera un momento')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
        elif 'qué hora es' in pedido:
            pedir_hora()
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido =  pedido.replace('buscando en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 1)
            hablar('wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Estoy en eso, espera un momento')
            print('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Claro!, comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada =  cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
                continue
        elif 'adios' in pedido:
            hablar('Hasta Luego mi chiquito hermoso')
            break


pedir()