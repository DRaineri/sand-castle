import pyglet
import game 

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
        self.bg_img = pyglet.image.load('images/chest/idle/menu_bg.png')
        self.bg = pyglet.sprite.Sprite(self.bg_img)
    
        self.t_y = 0

        self.width, self.height = args[:2]

        def_x = 50
        self.title = pyglet.text.Label("Tropical dreams", font_name='Duxbury Beach', font_size=95, x=def_x, y=self.height//2, anchor_x='left', anchor_y='center')
        self.title.color = (0,0,0,255)
        self.new_game = pyglet.text.Label("New game", font_name='Ubuntu', font_size=40,x=def_x, y=self.height//2, anchor_x='left', anchor_y='center')
        self.exit = pyglet.text.Label("Exit", font_name='Ubuntu', font_size=40,x=def_x, y=self.height//2, anchor_x='left', anchor_y='center')
        
        self.selected = 0

        self.labels = [self.new_game, self.exit]

        # Setting an update frequency of 60hz
        pyglet.clock.schedule_interval(self.update, 1.0 / 60)
    
    def update(self, dt):
        self.t_y += 4

    def on_draw(self):
        self.bg.draw()

        self.title.y = min(self.t_y,  self.height - 100)
        self.new_game.y = min(self.t_y - 800, self.height - 400)
        self.exit.y = min(self.t_y - 900, self.height - 500)

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
                w = game.GameWindow(1600, 800)
                self.close()
            elif self.labels[self.selected] == self.exit:
                self.close()

if __name__ == '__main__' :
    m = MenuWindow(1500, 800)
    pyglet.app.run()

