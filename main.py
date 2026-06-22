import pygame

pygame.init()

ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake Tech")

reloj = pygame.time.Clock()

x = 300
y = 200

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                x = x + 20

    ventana.fill((255, 255, 255))
    
    pygame.draw.rect(
        ventana,
        (0, 255, 0),
        (x, y, 20, 20)
    )
    
    
    reloj.tick(60)
    
    pygame.display.update()
