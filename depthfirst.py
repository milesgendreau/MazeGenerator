import random

def addPos(a, b):
    return (a[0]+b[0], a[1]+b[1])

class Cell():
    def __init__(self, x, y, w=20, h=12):
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

cells = []
for i in range(12):
    cells.append([])
    for j in range(20):
        cells[i].append(Cell(j, i))


prevVis = []
initial = cells[0][0]
initial.visited = True
prevVis.append(initial)
def depthFirst():
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
            

depthFirst()





    
