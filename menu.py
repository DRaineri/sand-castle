import pyglet


class MenuWindow(pyglet.window.Window):


    def update(self, dt):
        pass

    def __init__(self, *args, **kwargs):
        super(MenuWindow, self).__init__(*args, **kwargs)
    
        self.width, self.height = args[:2]

        self.label = pyglet.text.Label('Sable Castle', font_name='Comic sans MS', font_size=70,x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')
         # Setting an update frequency of 60hz
        pyglet.clock.schedule_interval(self.update, 1.0 / 60)
    

    def update(self, dt):
        pass


if __name__ == '__main__' :
    m = MenuWindow(800,600)
    pyglet.app.run()

