class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, character, screen_width, screen_height):
        self.x += (character.x - self.x - screen_width / 2 + character.width / 2) / 10
        self.y += (character.y - self.y - screen_height / 2 + character.height / 2) / 10