import os.path
import pygame

running = True

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1000, 600))
font = pygame.font.Font(None, 24)

generateButton = pygame.Rect(0, 0, 100, 60)

def drawButton(rect):
    pygame.draw.rect(display, (100, 100, 100), rect)
    text = font.render("Generate", True, (0, 0, 0))
    display.blit(text, (0, 0))

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos
                if generateButton.collidepoint(mousePos):
                    print("button pressed!")
         
    display.fill((255, 255, 255))
    drawButton(generateButton)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
