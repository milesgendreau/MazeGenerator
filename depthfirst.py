import random
import pygame

def addPos(a, b):
    # adds two positions, used for finding a cells neighbor
    
    return (a[0]+b[0], a[1]+b[1])

class Cell():
    # cells make up the grid and are stored within a 2-d list
    
    def __init__(self, x, y, w=40, h=30):
        self.pos = (x, y)
        self.mazeSize = (w, h) # used to check boundaries when searching for neighboring cells
        self.walls = [1, 1, 1, 1] # each cell starts with 4 walls, which are removed as the search moves through the grid
        self.visited = False

    def draw(self, display, dispScl):
        # draws a line for each remaining wall. Size and position are scaled based on the number of cells in the grid
        
        if self.walls[0] == 1:
            pygame.draw.line(display, (0,0,0), (self.pos[0]*dispScl, self.pos[1]*dispScl), (self.pos[0]*dispScl, (self.pos[1]+1)*dispScl))
        if self.walls[1] == 1:
            pygame.draw.line(display, (0,0,0), (self.pos[0]*dispScl, self.pos[1]*dispScl), ((self.pos[0]+1)*dispScl, self.pos[1]*dispScl))
        if self.walls[2] == 1:
            pygame.draw.line(display, (0,0,0), ((self.pos[0]+1)*dispScl, self.pos[1]*dispScl), ((self.pos[0]+1)*dispScl, (self.pos[1]+1)*dispScl))
        if self.walls[3] == 1:
            pygame.draw.line(display, (0,0,0), (self.pos[0]*dispScl, (self.pos[1]+1)*dispScl), ((self.pos[0]+1)*dispScl, (self.pos[1]+1)*dispScl))

    def findNeighbor(self, cells, opt):
        # chooses a neighboring cell randomly, recursively eliminates options.
        # choices need to be random to ensure the final maze is random
        
        options = opt
        visit = random.choice(options)
        sumVisit = addPos(self.pos, visit)
        if min(sumVisit) >= 0 and sumVisit[0] < self.mazeSize[0] and sumVisit[1] < self.mazeSize[1]:
            neighbor = cells[sumVisit[1]][sumVisit[0]]
            if neighbor.visited == False:
                return neighbor, visit
            else:
                options.remove(visit)
                if len(options) > 0:
                    return self.findNeighbor(cells, options)
                else:
                    return 0, 0
    
        else:
            options.remove(visit)
            if len(options) > 0:
                return self.findNeighbor(cells, options)
            else:
                return 0, 0         

def initializeCells(w, h):
    cells = []
    for i in range(h):
        cells.append([])
        for j in range(w):
            cells[i].append(Cell(j, i, w, h))

    return cells


def depthFirst(w=40, h=30):
    cells = initializeCells(w, h)

    prevVis = [] # stack of previously visited cells, implemented here with a list using .append() and .pop()
    initial = cells[random.randint(0, h-1)][random.randint(0, w-1)]
    #initial = cells[-1][-1]
    initial.visited = True
    prevVis.append(initial)

    while len(prevVis) > 0:
        # randomly visits neighboring cells until it reaches a corner, then backtracks
        
        current = prevVis.pop()
        neighbor, visit = current.findNeighbor(cells, [(-1, 0), (0, -1), (1, 0), (0, 1)]) # neighboring cell and direction from whence it was chosen
        if neighbor != 0:
            prevVis.append(current)

            # removes the walls between the current cell and the cell it is moving to
            if visit == (1, 0):
                current.walls[2] = 0
                neighbor.walls[0] = 0
            elif visit == (-1, 0):
                current.walls[0] = 0
                neighbor.walls[2] = 0
            elif visit == (0, 1):
                current.walls[3] = 0
                neighbor.walls[1] = 0
            elif visit == (0, -1):
                current.walls[1] = 0
                neighbor.walls[3] = 0

            neighbor.visited = True
            prevVis.append(neighbor)

    cells[0][0].walls[0] = 0 # entance
    cells[-1][-1].walls[2] = 0 # exit

    return cells

def drawCells(cells, display, dispScl):
    for row in cells:
        for cell in row:
            cell.draw(display, dispScl)

def getSize():
    try:
        return (int(input("width?: ")), int(input("height?: ")))
    except:
        return getSize()

size = getSize()
cells = depthFirst(size[0], size[1])





    
