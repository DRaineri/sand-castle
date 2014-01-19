import pyglet


class MenuWindow(pyglet.window.Window):



    def __init__(self, *args, **kwargs):
        super(MenuWindow, self).__init__(*args, **kwargs)

        bg_color = pyglet.image.SolidColorImagePattern(color=(20, 20, 30, 255))
        self.bg_img = bg_color.create_image(self.width, self.height)
        self.bg = pyglet.sprite.Sprite(self.bg_img)
    

        self.t_y = 0

        self.width, self.height = args[:2]

        self.title = pyglet.text.Label("Tropical dreams", font_name='Stainy Personal Use Only', font_size=70,x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')
        
        self.new_game = pyglet.text.Label("New game", font_name='Ubuntu', font_size=40,x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')
        self.exit = pyglet.text.Label("Exit", font_name='Ubuntu', font_size=40,x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')
        

        # Setting an update frequency of 60hz
        pyglet.clock.schedule_interval(self.update, 1.0 / 60)
    
    def update(self, dt):
        self.t_y += 4

    def on_draw(self):
        self.bg.draw()

        self.title.y = min(self.t_y,  self.height - 250)
        self.title.draw()
        
        self.new_game.y = min(self.t_y - 800, self.height - 500)
        self.exit.y = min(self.t_y - 900, self.height - 600)

        self.title.draw()
        self.new_game.draw()
        self.exit.draw()

if __name__ == '__main__' :
    m = MenuWindow(1024, 800)
    pyglet.app.run()

