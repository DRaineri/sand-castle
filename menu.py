import pyglet
from game import GameWindow

def draw_with_shadow(label, s_label=None):
    bak_color = label.color
    if label == s_label:
        label.color = (80, 80, 150, 255)

    label.draw()
    label.x -= 1
    label.y -= 1
    label.color = (0, 0, 0, 60)
    label.draw()
    label.x += 1
    label.y += 1
    label.color = bak_color



class MenuWindow(pyglet.window.Window):



    def __init__(self, *args, **kwargs):
        super(MenuWindow, self).__init__(*args, **kwargs)

        bg_color = pyglet.image.SolidColorImagePattern(color=(80, 80, 80, 255))
        self.bg_img = bg_color.create_image(self.width, self.height)
        self.bg = pyglet.sprite.Sprite(self.bg_img)
    
        self.t_y = 0

        self.width, self.height = args[:2]

        self.title = pyglet.text.Label("Tropical dreams", font_name='Stainy Personal Use Only', font_size=70,x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')
        
        self.new_game = pyglet.text.Label("New game", font_name='Ubuntu', font_size=40,x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')
        self.exit = pyglet.text.Label("Exit", font_name='Ubuntu', font_size=40,x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')
        
        self.selected = 0

        self.labels = [self.new_game, self.exit]

        # Setting an update frequency of 60hz
        pyglet.clock.schedule_interval(self.update, 1.0 / 60)
    
    def update(self, dt):
        self.t_y += 4

    def on_draw(self):
        self.bg.draw()

        self.title.y = min(self.t_y,  self.height - 250)
        self.new_game.y = min(self.t_y - 800, self.height - 500)
        self.exit.y = min(self.t_y - 900, self.height - 600)

        draw_with_shadow(self.title)

        s_label = self.labels[self.selected]
        draw_with_shadow(self.new_game, s_label)
        draw_with_shadow(self.exit, s_label)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP:
            self.selected = (self.selected + 1) % len(self.labels)
        elif symbol == pyglet.window.key.DOWN:
            self.selected = (self.selected - 1) % len(self.labels)
        elif symbol == pyglet.window.key.ENTER:
            if self.labels[self.selected] == self.new_game:
                w = GameWindow(1200, 800)
            elif self.labels[self.selected] == self.exit:
                self.close()

if __name__ == '__main__' :
    m = MenuWindow(1024, 800)
    pyglet.app.run()

