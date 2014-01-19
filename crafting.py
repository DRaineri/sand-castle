import pyglet

class Screen_craft(object):
    """docstring for Screen_craft"""
    def __init__(self):
        super(Screen_craft, self).__init__()

    def run_crafting(self):
        self.background_image = pyglet.image.load("./images/crafting/background_crafting.png")
        self.background = pyglet.sprite.Sprite(self.background_image, 0, 0)
    
    def draw(self):
        self.background.draw()

