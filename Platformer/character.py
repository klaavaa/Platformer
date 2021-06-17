from attributes import GRAVITY
from object import Object
from collider import Collider
class Character(Object):
    def __init__(self):
        super().__init__(0, 500, 64, 64)

        self.x_vel = 0
        self.y_vel = 1

        self.max_jump_vel = -1000
        self.min_jump_vel = -500

        self.is_on_ground = True
        self.has_jumped = False

        self.collider = Collider(self)


    def update(self, dt, world):
        #position += velocity * delta + acceleration * delta * delta * 0.5

        self.collider.move_and_collide(dt, world)


        self.y_vel += GRAVITY*dt

    def draw(self, rect, win, cx, cy):
        rect(win, (255, 0, 0), (self.x - cx, self.y - cy, self.width, self.height), 1)