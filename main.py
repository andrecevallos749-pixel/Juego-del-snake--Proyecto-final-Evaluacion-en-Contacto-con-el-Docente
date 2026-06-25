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

tipo_comida = "normal"
tiempo_comida = pygame.time.get_ticks()

puntos = 0

direccion_x = 0
direccion_y = 0

velocidad_base = 5
velocidad = velocidad_base

turbo_activo = False
tiempo_turbo = 0

escudo_activo = False
tiempo_escudo = 0

estado = "menu"


while True:

    if estado == "menu":
        ventana.fill((245, 245, 245))

        titulo = fuente.render("SNAKE TECH", True, (0,120,0))
        titulo_rect = titulo.get_rect(center=(ANCHO//2, 90))
        ventana.blit(titulo, titulo_rect)

        boton_iniciar = pygame.Rect(220, 190, 200, 55)
        boton_salir   = pygame.Rect(220, 265, 200, 55)
        
        mouse = pygame.mouse.get_pos()

        if boton_iniciar.collidepoint(mouse):
           color_iniciar = (0, 220, 0)
        else:
            color_iniciar = (0, 180, 0)

        if boton_salir.collidepoint(mouse):
           color_salir = (220, 0, 0)
        else:
           color_salir = (180, 0, 0)

        pygame.draw.rect(ventana, color_iniciar, boton_iniciar, border_radius=10)
        pygame.draw.rect(ventana, color_salir, boton_salir, border_radius=10)

        texto_iniciar = fuente.render("INICIAR", True, (255, 255, 255))
        texto_salir = fuente.render("SALIR", True, (255, 255, 255))
        
        
        ventana.blit(texto_iniciar, (275, 203))
        ventana.blit(texto_salir, (292, 278))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_iniciar.collidepoint(evento.pos):
                    estado = "dificultad"

                if boton_salir.collidepoint(evento.pos):
                   estado = "salir"

        continue
    
    if estado == "dificultad":
        ventana.fill((245, 245, 245))

        titulo = fuente.render("DIFICULTAD", True, (0, 120, 0))
        titulo_rect = titulo.get_rect(center=(ANCHO//2, 80))
        ventana.blit(titulo, titulo_rect)

        boton_facil = pygame.Rect(220, 150, 200, 50)
        boton_medio = pygame.Rect(220, 220, 200, 50)
        boton_dificil = pygame.Rect(220, 290, 200, 50)
        boton_volver = pygame.Rect(220, 360, 200, 45)

        mouse = pygame.mouse.get_pos()

        color_facil = (0, 220, 0) if boton_facil.collidepoint(mouse) else (0, 180, 0)
        color_medio = (220, 180, 0) if boton_medio.collidepoint(mouse) else (180, 140, 0)
        color_dificil = (220, 0, 0) if boton_dificil.collidepoint(mouse) else (180, 0, 0)
        color_volver = (120, 120, 120) if boton_volver.collidepoint(mouse) else (90, 90, 90)
        
        
        pygame.draw.rect(ventana, color_facil, boton_facil, border_radius=10)
        pygame.draw.rect(ventana, color_medio, boton_medio, border_radius=10)
        pygame.draw.rect(ventana, color_dificil, boton_dificil, border_radius=10)
        pygame.draw.rect(ventana, color_volver, boton_volver, border_radius=10)
        
        texto_facil = fuente.render("FACIL", True, (255, 255, 255))
        texto_medio = fuente.render("MEDIO", True, (255, 255, 255))
        texto_dificil = fuente.render("DIFICIL", True, (255, 255, 255))
        texto_volver = fuente.render("VOLVER", True, (255, 255, 255))
        
        ventana.blit(texto_facil, (270, 160))
        ventana.blit(texto_medio, (265, 230))
        ventana.blit(texto_dificil, (255, 300))
        ventana.blit(texto_volver, (275, 368))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if boton_facil.collidepoint(evento.pos):
                    velocidad_base = 5
                    velocidad = velocidad_base
                    estado = "jugando"

                if boton_medio.collidepoint(evento.pos):
                    velocidad_base = 8
                    velocidad = velocidad_base
                    estado = "jugando"

                if boton_dificil.collidepoint(evento.pos):
                    velocidad_base = 12
                    velocidad = velocidad_base
                    estado = "jugando"
                if boton_volver.collidepoint(evento.pos):
                   estado = "menu"

        continue
    
    if estado == "game_over":
        ventana.fill((245, 245, 245))

        titulo = fuente.render("GAME OVER", True, (255, 0, 0))
        titulo_rect = titulo.get_rect(center=(ANCHO//2, 90))
        ventana.blit(titulo, titulo_rect)

        texto_puntaje = fuente.render("Puntaje final: " + str(puntos), True, (0, 0, 0))
        texto_puntaje_rect = texto_puntaje.get_rect(center=(ANCHO//2, 145))
        ventana.blit(texto_puntaje, texto_puntaje_rect)

        boton_reintentar = pygame.Rect(220, 210, 200, 55)
        boton_dificultad = pygame.Rect(170, 290, 300, 55)
        boton_salir = pygame.Rect(220, 370, 200, 55)
        
        mouse = pygame.mouse.get_pos()

        color_reintentar = (0, 220, 0) if boton_reintentar.collidepoint(mouse) else (0, 180, 0)
        color_dificultad = (0, 120, 220) if boton_dificultad.collidepoint(mouse) else (0, 90, 180)
        color_salir = (220, 0, 0) if boton_salir.collidepoint(mouse) else (180, 0, 0)
        
        pygame.draw.rect(ventana, color_reintentar, boton_reintentar, border_radius=10)
        pygame.draw.rect(ventana, color_dificultad, boton_dificultad, border_radius=10)
        pygame.draw.rect(ventana, color_salir, boton_salir,border_radius=10)
        
        texto_reintentar = fuente.render("REINTENTAR", True, (255, 255, 255))
        texto_dificultad = fuente.render("CAMBIAR DIFICULTAD", True, (255, 255, 255))
        texto_rect = texto_dificultad.get_rect(center=boton_dificultad.center)
        ventana.blit(texto_dificultad, texto_rect)
        
        texto_salir = fuente.render("SALIR", True, (255, 255, 255))
        ventana.blit(texto_salir, (292, 385))

        ventana.blit(texto_reintentar,  (245, 225))
       

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if boton_reintentar.collidepoint(evento.pos):
                    x = 300
                    y = 200
                    direccion_x = 0
                    direccion_y = 0
                    serpiente = []
                    longitud_serpiente = 1
                    puntos = 0
                    turbo_activo = False
                    escudo_activo = False
                    velocidad = velocidad_base
                    comida_x = random.randrange(0, ANCHO, tamano)
                    comida_y = random.randrange(0, ALTO, tamano)
                    tipo_comida = "normal"
                    tiempo_comida = pygame.time.get_ticks()
                    estado = "jugando"
                    
                if boton_dificultad.collidepoint(evento.pos):
                    x = 300
                    y = 200
                    direccion_x = 0
                    direccion_y = 0
                    serpiente = []
                    longitud_serpiente = 1
                    puntos = 0
                    turbo_activo = False
                    escudo_activo = False
                    tipo_comida = "normal"
                    comida_x = random.randrange(0, ANCHO, tamano)
                    comida_y = random.randrange(0, ALTO, tamano)
                    tiempo_comida = pygame.time.get_ticks()

                    estado = "dificultad"
                    
                if boton_salir.collidepoint(evento.pos):
                    estado = "salir"

        continue
    if estado == "salir":

            ventana.fill((245, 245, 245))

            texto1 = fuente.render("¡Gracias por jugar!", True, (0, 120, 0))
            texto2 = fuente.render("Snake Tech", True, (0, 0, 0))

            rect1 = texto1.get_rect(center=(ANCHO//2, 200))
            rect2 = texto2.get_rect(center=(ANCHO//2, 245))

            ventana.blit(texto1, rect1)
            ventana.blit(texto2, rect2)

            pygame.display.update()

            pygame.time.delay(2500)

            pygame.quit()
            exit()
    
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

     if escudo_activo:
        escudo_activo = False

        if x < 0:
            x = 0
        if x > ANCHO - tamano:
            x = ANCHO - tamano
        if y < 0:
            y = 0
        if y > ALTO - tamano:
            y = ALTO - tamano

     else:
        estado = "game_over"
        continue

    cabeza = (x, y)
    serpiente.append(cabeza)
    
    if longitud_serpiente > 4 and cabeza in serpiente[:-1]:

     if escudo_activo:
        escudo_activo = False

     else:
        estado = "game_over"
        continue
    
   
    if x == comida_x and y == comida_y:
        
        print(tipo_comida)
     
        if tipo_comida == "normal":
         puntos = puntos + 1
         longitud_serpiente = longitud_serpiente + 1

        if tipo_comida == "dorada":
          puntos = puntos + 5
          longitud_serpiente = longitud_serpiente + 1
          
        if tipo_comida == "trampa":
            
            puntos = puntos - 1

            if longitud_serpiente > 1:
             longitud_serpiente = max(1, int(longitud_serpiente * 0.5))

            while len(serpiente) > longitud_serpiente:
              serpiente.pop(0)
              
        if tipo_comida == "azul":
            
            puntos = puntos + 1
            longitud_serpiente = longitud_serpiente + 1
            
            turbo_activo = True
            tiempo_turbo = pygame.time.get_ticks()
            velocidad = velocidad_base + 5

        if tipo_comida == "escudo":

          puntos = puntos + 1
          longitud_serpiente = longitud_serpiente + 1
          
          escudo_activo = True
          tiempo_escudo = pygame.time.get_ticks()
        
        if puntos > 0 and puntos % 5 == 0:
         velocidad_base = velocidad_base + 1

         if not turbo_activo:
          velocidad = velocidad_base
        
        print("Comiste la comida")
        print("Puntos:", puntos)

        comida_x = random.randrange(0, ANCHO, tamano)
        comida_y = random.randrange(0, ALTO, tamano)
        
        tipo_comida = random.choice(["normal", "normal", "normal", "dorada", "trampa", "azul", "escudo"])
        
        tiempo_comida = pygame.time.get_ticks()

    if len(serpiente) > longitud_serpiente:
        serpiente.pop(0)
    
    if tipo_comida != "normal":

     tiempo_actual = pygame.time.get_ticks()

     if tiempo_actual - tiempo_comida > 5000:

        comida_x = random.randrange(0, ANCHO, tamano)
        comida_y = random.randrange(0, ALTO, tamano)

        tipo_comida = random.choice(
            ["normal", "normal", "normal", "dorada", "trampa", "azul", "escudo"])

        tiempo_comida = pygame.time.get_ticks()
    
    if turbo_activo:
         tiempo_actual = pygame.time.get_ticks()

         if tiempo_actual - tiempo_turbo > 5000:
           turbo_activo = False
           velocidad = velocidad_base
           
    if escudo_activo:

        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - tiempo_escudo > 10000:
          escudo_activo = False

    ventana.fill((255, 255, 255))

    for parte in serpiente[:-1]:
      pygame.draw.rect(
        ventana,
        (0, 200, 0),
        (parte[0], parte[1], tamano, tamano))

    if escudo_activo:
     color_cabeza = (180, 180, 180)
    elif turbo_activo:
     color_cabeza = (0, 0, 255)
    else:
     color_cabeza = (0, 120, 0)

    pygame.draw.rect(
     ventana,
     color_cabeza,
     (serpiente[-1][0], serpiente[-1][1], tamano, tamano))

    if tipo_comida == "normal":
     color_comida = (255, 0, 0)

    if tipo_comida == "dorada":
     color_comida = (255, 215, 0)
     
    if tipo_comida == "trampa":
       color_comida = (148, 0, 211)
       
    if tipo_comida == "azul":
       color_comida = (0, 0, 255)
       
    if tipo_comida == "escudo":
       color_comida = (180, 180, 180)

    pygame.draw.rect(
     ventana,
     color_comida,
     (comida_x, comida_y, tamano, tamano))

    texto_puntos = fuente.render("Puntos: " + str(puntos), True, (0, 0, 0))
    ventana.blit(texto_puntos, (10, 10))

    if turbo_activo:
      tiempo_restante_turbo = 5 - (pygame.time.get_ticks() - tiempo_turbo) // 1000

      texto_turbo = fuente.render(
        "Turbo: " + str(tiempo_restante_turbo) + "s", True,
        (0, 0, 255))

      ventana.blit(texto_turbo, (10, 40))

    if escudo_activo:
     tiempo_restante_escudo = 10 - (pygame.time.get_ticks() - tiempo_escudo) // 1000

     texto_escudo = fuente.render(
        "Escudo: " + str(tiempo_restante_escudo) + "s",
        True,
        (120, 120, 120))

     ventana.blit(texto_escudo, (10, 70))

    pygame.display.update()
    reloj.tick(velocidad)
    