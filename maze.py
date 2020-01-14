import pygame
from depthfirst import cells, size

pygame.init()
dispScl = int(1000/size[0])
display = pygame.display.set_mode((size[0]*dispScl, size[1]*dispScl))
display.fill((255, 255, 255))
pygame.display.update()
running = True

def drawCell(cell):
    if cell.walls[0] == 1:
        pygame.draw.line(display, (0,0,0), (cell.pos[0]*dispScl, cell.pos[1]*dispScl), (cell.pos[0]*dispScl, (cell.pos[1]+1)*dispScl))
    if cell.walls[1] == 1:
        pygame.draw.line(display, (0,0,0), (cell.pos[0]*dispScl, cell.pos[1]*dispScl), ((cell.pos[0]+1)*dispScl, cell.pos[1]*dispScl))
    if cell.walls[2] == 1:
        pygame.draw.line(display, (0,0,0), ((cell.pos[0]+1)*dispScl, cell.pos[1]*dispScl), ((cell.pos[0]+1)*dispScl, (cell.pos[1]+1)*dispScl))
    if cell.walls[3] == 1:
        pygame.draw.line(display, (0,0,0), (cell.pos[0]*dispScl, (cell.pos[1]+1)*dispScl), ((cell.pos[0]+1)*dispScl, (cell.pos[1]+1)*dispScl))

for row in cells:
    for cell in row:
        drawCell(cell)

pygame.display.update()

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
quit()
