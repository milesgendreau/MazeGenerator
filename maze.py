import os.path
import pygame, thorpy

running = True
pygame.init()
screenSize = (1000, 600)
icon = pygame.image.load("icon.png")

pygame.display.set_caption("Maze Generator")
pygame.display.set_icon(icon)
display = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()


while running:
    clock.tick(60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    display.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
quit()
