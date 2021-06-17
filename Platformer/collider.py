
class Collider:
    def __init__(self, object):
        self.object = object
        self.dx = self.object.x
        self.dy = self.object.y

    def AABB(self, other):
        return (self.object.x < other.object.x + other.object.width and
                self.object.x + self.object.width > other.object.x and
                self.object.y < other.object.y + other.object.height and
                self.object.y + self.object.height > other.object.y)


    def response(self, world):
        for obstacle in world.obstacles:
            if self.AABB(obstacle.collider):
                return True

        return False

    def move_and_collide(self, dt, world):

        self.dy = self.object.y
        self.object.y += self.object.y_vel * dt
        if self.response(world):
            self.object.y = self.dy
            self.object.is_on_ground = True
            self.object.has_jumped = False
            self.object.y_vel = 0
        else:
            self.object.is_on_ground = False
        self.dx = self.object.x
        self.object.x += self.object.x_vel * dt
        if self.response(world):
            self.object.x = self.dx

        self.object.x_vel = 0




