class Cell():
    def __init__(x, y, w=100, h=100):
        self.pos = (x, y)
        self.visited = False
        if x > 0 and x < w:
            if y > 0 and y < h:
                self.neighbors = 4
            else:
                self.neighbors = 3
        elif y > 0 and y < h:
            self.neighbors = 3
        else:
            self.neighbors = 2

cells = []
for i in range(100):
    for j in range(100):
        cells.append(Cell(j, i))

def adjCell(num):
    if num == 0:
        return (-1, 0)
    elif num == 1:
        return (0, -1)
    elif num == 2:
        return (1, 0)
    elif num == 3:
        return (0, 1)
    else:
        return

def sumPos(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

current_cell = (random.randint(0, 100), random.randint(0, 100))

def search():
    visit = adjCell(random.randint(0, 4))
        

    

