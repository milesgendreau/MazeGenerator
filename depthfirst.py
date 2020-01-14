import random

def addPos(a, b):
    return (a[0]+b[0], a[1]+b[1])

class Cell():
    def __init__(self, x, y, w=40, h=30):
        self.pos = (x, y)
        self.mazeSize = (w, h)
        self.walls = [1, 1, 1, 1]
        self.visited = False

    def findNeighbor(self, cells, opt):
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

def depthFirst(w=40, h=30):
    cells = []
    for i in range(h):
        cells.append([])
        for j in range(w):
            cells[i].append(Cell(j, i, w, h))


    prevVis = []
    initial = cells[0][0]
    initial.visited = True
    prevVis.append(initial)

    while len(prevVis) > 0:
        current = prevVis.pop()
        neighbor, visit = current.findNeighbor(cells, [(-1, 0), (0, -1), (1, 0), (0, 1)])
        if neighbor != 0:
            prevVis.append(current)
            
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

    return cells
            

def getSize():
    try:
        return (int(input("width?: ")), int(input("height?: ")))
    except:
        return getSize()

size = getSize()
cells = depthFirst(size[0], size[1])





    
