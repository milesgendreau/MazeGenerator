import os.path
import pygame
import depthfirst

running = True

pygame.init()
dispScl = int(1000/depthfirst.size[0])
display = pygame.display.set_mode((depthfirst.size[0]*dispScl + 1, depthfirst.size[1]*dispScl + 1))
display.fill((255, 255, 255))

depthfirst.drawCells(depthfirst.cells, display, dispScl)
pygame.display.update()

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    count = 0
                    fname = "mazes\df" + str(depthfirst.size[0]) + "x" + str(depthfirst.size[1]) + "(" + str(count) + ")" + ".png"
                    while os.path.exists(fname):
                        count += 1
                        fname = "mazes\df" + str(depthfirst.size[0]) + "x" + str(depthfirst.size[1]) + "(" + str(count) + ")" + ".png"
                    pygame.image.save(display, fname)
                    print("Image Saved!")

pygame.quit()
quit()
