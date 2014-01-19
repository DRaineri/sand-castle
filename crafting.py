import pyglet

class Screen_craft(object):
    """docstring for Screen_craft"""
    def __init__(self, game):
        super(Screen_craft, self).__init__()
        self.game = game

    def run_crafting(self):
        self.background_image = pyglet.image.load("./images/crafting/background_crafting.png")
        self.background = pyglet.sprite.Sprite(self.background_image, self.game.width/2 - self.background_image.width/2, self.game.height/2 - self.background_image.height/2)

        pos_x_symbole = self.game.width/2 - self.background_image.width/2 + 20
        pos_x_text = self.game.width/2 - self.background_image.width/2 + 440
        pos_y_symbole = self.game.height/2 - self.background_image.height/2 + 20
        pos_y_text = self.game.height/2 - self.background_image.height/2 + 60

        self.ruby_image = pyglet.image.load("./images/crafting/ruby.png")
        self.ruby = pyglet.sprite.Sprite(self.ruby_image, pos_x_symbole, pos_y_symbole)

        self.definition_1 = pyglet.text.Label(text="Evoluer le chateau", font_name="Ubuntu", bold=True, font_size=24,
                                       x=pos_x_text, y=pos_y_text, anchor_x='right', anchor_y='top')
    
    def draw(self):
        self.background.draw()
        self.ruby.draw()
        self.definition_1.draw()

