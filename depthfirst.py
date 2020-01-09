class Cell():
    def __init__(x, y, w=, h=):
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

