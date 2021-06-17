from collider import Collider
from object import Object
class Obstacle(Object):
    def __init__(self,x, y, width, height):
        super().__init__(x, y, width, height)
        self.collider = Collider(self)


    def draw(self, rect, win, cx, cy):
        rect(win, (255, 255, 255), (self.x - cx, self.y - cy, self.width, self.height))