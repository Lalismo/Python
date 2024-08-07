import pygame
import random
import math
from pygame import mixer
import io

#Inizializar pygame
pygame.init()

#Crear el tamaño que queremos que tenga nuestra pantalla
pantalla = pygame.display.set_mode((800,600))

#Crearmos una variable para el evento de quitar
ejecuta = True

#Titulo e Icono
pygame.display.set_caption('Invacion espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

#Musica de fondo
mixer.music.load('musica.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#Variables del jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#Variables de los enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8


for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(50)

#Variables de la bala
balas = []
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

#Funcion para transformar nuestra fuente a bytes
def fuente_bytes(fuente):
    #Abrir el archivo TTF en modo lentura binaria
    with open(fuente, 'rb') as f:
        #Leer todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
        #Crea un objeto BytesIO a partir de los bytes del archivo TTF
        return io.BytesIO(ttf_bytes)


# Puntaje
puntaje = 0
fuente_en_bytes = fuente_bytes('FreeSansBold.ttf')
fuente = pygame.font.Font(fuente_en_bytes, 32)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_final = pygame.font.Font(fuente_en_bytes, 40)

# Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

# Funcion enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y))

# Funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible =  True
    pantalla.blit(img_bala, (x+16,y+10))

# Funcion detectar colicion
def colision(x1,y1,x2,y2):
    distancia =  math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False
    
# Funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))
    pantalla.blit(texto, (x,y))

#Funcion para texto final
def texto_final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255,255,255))
    pantalla.blit(mi_fuente_final, (250,200))




# Hacemos un loop while que itere y muestre la pantalla hasta que el evento QUIT sea llamado y se cierre
while ejecuta:

    # Imagen de fondo
    pantalla.blit(fondo,(0,0))
    # Iteracion de eventos
    for evento in pygame.event.get():
        # Evento cerrar ventana
        if evento.type == pygame.QUIT:
            ejecuta = False
        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                nueva_bala = {
                "x": jugador_x,
                "y": jugador_y,
                "velocidad": -1
                }
                balas.append(nueva_bala)

        # Evento soltar tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicacion del jugador en eje x
    jugador_x +=  jugador_x_cambio

    # Mantener dentro del borde al jugador
    if jugador_x <=0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicacion del enemigo en eje y
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] +=  enemigo_x_cambio[e]

    # Mantener dentro del borde al enemigo
        if enemigo_x[e] <=0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # Movimiento bala
        for bala in balas:
            bala["y"] += bala["velocidad"]
            pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
            if bala["y"] < 0:
                balas.remove(bala)

        # Colision de la bala
        for bala in balas:

            pego = colision(enemigo_x[e],enemigo_y[e], bala['x'], bala['y'])
        
            if pego:
                sonido_colision = mixer.Sound('golpe.mp3')
                sonido_colision.play()
                balas.remove(bala)
                bala_visible = False
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50,200)
                break

        enemigo(enemigo_x[e],enemigo_y[e], e)

    jugador(jugador_x,jugador_y)
    mostrar_puntaje(texto_x,texto_y)
    
    # Actualizar la pantalla por cada iteracion
    pygame.display.update()
