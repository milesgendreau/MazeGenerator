import pygame
from depthfirst import cells

pygame.init()
display = pygame.display.set_mode((1000, 600))
display.fill((255, 255, 255))
pygame.display.update()
running = True

def drawCell(cell):
    if cell.walls[0] == 1:
        pygame.draw.line(display, (0,0,0), (cell.pos[0]*50, cell.pos[1]*50), (cell.pos[0]*50, (cell.pos[1]+1)*50))
    if cell.walls[1] == 1:
        pygame.draw.line(display, (0,0,0), (cell.pos[0]*50, cell.pos[1]*50), ((cell.pos[0]+1)*50, cell.pos[1]*50))
    if cell.walls[2] == 1:
        pygame.draw.line(display, (0,0,0), ((cell.pos[0]+1)*50, cell.pos[1]*50), ((cell.pos[0]+1)*50, (cell.pos[1]+1)*50))
    if cell.walls[3] == 1:
        pygame.draw.line(display, (0,0,0), (cell.pos[0]*50, (cell.pos[1]+1)*50), ((cell.pos[0]+1)*50, (cell.pos[1]+1)*50))

for row in cells:
    for cell in row:
        #pygame.draw.rect(display, (0,0,0), (cell.pos[0]*10, cell.pos[1]*10, 10, 10), 1)
        drawCell(cell)

pygame.display.update()

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
quit()
