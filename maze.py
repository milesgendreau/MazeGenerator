import pygame

pygame.init()
display = pygame.display.set_mode((800, 500))
display.fill((255, 255, 255))
pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
quit()
