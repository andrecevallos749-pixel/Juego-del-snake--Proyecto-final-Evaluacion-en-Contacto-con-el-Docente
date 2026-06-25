import pygame
import random

pygame.init()

ANCHO = 640
ALTO = 480

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Tech")

fuente = pygame.font.SysFont("Arial", 25)
reloj = pygame.time.Clock()

x = 300
y = 200
tamano = 20

serpiente = []
longitud_serpiente = 1

comida_x = 100
comida_y = 100

puntos = 0

direccion_x = 0
direccion_y = 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                direccion_x = tamano
                direccion_y = 0

            if evento.key == pygame.K_LEFT:
                direccion_x = -tamano
                direccion_y = 0

            if evento.key == pygame.K_UP:
                direccion_x = 0
                direccion_y = -tamano

            if evento.key == pygame.K_DOWN:
                direccion_x = 0
                direccion_y = tamano

    x = x + direccion_x
    y = y + direccion_y

    if x < 0 or x > ANCHO - tamano or y < 0 or y > ALTO - tamano:
     ventana.fill((255, 255, 255))

     texto_game_over = fuente.render("GAME OVER", True, (255, 0, 0))
     texto_puntaje = fuente.render("Puntaje final: " + str(puntos), True, (0, 0, 0))

     ventana.blit(texto_game_over, (250, 200))
     ventana.blit(texto_puntaje, (230, 240))

     pygame.display.update()
     pygame.time.delay(3000)

     pygame.quit()
     exit()

    cabeza = (x, y)
    serpiente.append(cabeza)
    
    if longitud_serpiente > 4 and cabeza in serpiente[:-1]:
     ventana.fill((255, 255, 255))

     texto_game_over = fuente.render("GAME OVER", True, (255, 0, 0))
     texto_puntaje = fuente.render("Puntaje final: " + str(puntos), True, (0, 0, 0))

     ventana.blit(texto_game_over, (250, 200))
     ventana.blit(texto_puntaje, (230, 240))

     pygame.display.update()
     pygame.time.delay(3000)

     pygame.quit()
     exit()
    
   
    if x == comida_x and y == comida_y:
        puntos = puntos + 1
        longitud_serpiente = longitud_serpiente + 1
        print("Comiste la comida")
        print("Puntos:", puntos)

        comida_x = random.randrange(0, ANCHO, tamano)
        comida_y = random.randrange(0, ALTO, tamano)

    if len(serpiente) > longitud_serpiente:
        serpiente.pop(0)

    ventana.fill((255, 255, 255))

    for parte in serpiente[:-1]:
      pygame.draw.rect(
        ventana,
        (0, 200, 0),
        (parte[0], parte[1], tamano, tamano))

    pygame.draw.rect(
       ventana,
       (0, 120, 0),
       (serpiente[-1][0], serpiente[-1][1], tamano, tamano))

    pygame.draw.rect(
        ventana,
        (255, 0, 0),
        (comida_x, comida_y, tamano, tamano))

    texto_puntos = fuente.render("Puntos: " + str(puntos), True, (0, 0, 0))
    ventana.blit(texto_puntos, (10, 10))

    pygame.display.update()
    reloj.tick(5)