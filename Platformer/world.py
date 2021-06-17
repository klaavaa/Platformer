class World:
    def __init__(self, character, camera):
        self.obstacles = []
        self.character = character
        self.camera = camera
    def get_objects(self):
        return self.obstacles