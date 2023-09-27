class Scene:
    def __init__(self):
        self.scene_objects = list()

    def draw(self):
        for object in self.scene_objects:
            object.run()
