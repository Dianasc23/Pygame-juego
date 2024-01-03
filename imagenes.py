import pygame

pygame.init()
screen = pygame.display.set_mode([720, 720])
clock = pygame.time.Clock()

done = False

background = pygame.image.load('cocina.jpg').convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.blit(background, [100, 100])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
