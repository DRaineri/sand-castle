import random
import config
import pyglet

from elements import Character
from math import cos

def random_bg():
    return random.choice([Sand, Jungle, Sea])

class Grid(object):
    def __init__(self, w, h):
        self.grid = [[ None for x in xrange(w)] for y in xrange(h)]

        self.w = w
        self.h = h
        self.populate()


    def populate(self):
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                r_x, r_y = x * config.CELL_SIZE, y * config.CELL_SIZE
                if x<1:
                    self.grid[y][x] = Sea(r_x, r_y)
                elif x==1:
                    self.grid[y][x] = SeaBorder(r_x, r_y)
                elif x>(self.w-4):
                    self.grid[y][x] = Jungle(r_x, r_y)
                else:
                    self.grid[y][x] = Sand(r_x, r_y)
                
                
    def draw_background(self):
        for row in self.grid:
            for cell in row:
                cell.background.draw()

    def draw_foreground(self):
        for row in self.grid:
            for cell in row:
                if cell.foreground:
                    cell.foreground.draw()
                    cell.update()

    def neighbours(self, element):
        neigh = []
        b_x = int(element.x // config.CELL_SIZE) - 1
        b_y = int(element.y // config.CELL_SIZE) - 1

        for x in xrange(b_x, b_x + element.w + 2):
            for y in xrange(b_y, b_y + element.h + 2):
                valid_coords = 0 <= x < self.w and 0 <= y < self.h
                if not valid_coords:
                    continue
                el = self.grid[y][x].element
                valid_neighbour = not el is None and el != element and not el in neigh
                if valid_coords and valid_neighbour:
                    neigh.append(self.grid[y][x].element)

        return neigh

    def update_elements(self, elements):
        for row in self.grid:
            for cell in row:
                cell.element = None

        for element in elements:
            if not element.is_collidable():
                continue
            for x, y in element.cells():
                self.grid[y][x].element = element


class Cell(object):
    def __init__(self,x,y, element=None):
        self.element = element
        image_population = [image for (image, weight) in self.images for i in xrange(weight)]
        self.background = pyglet.sprite.Sprite(random.choice(image_population), x, y)
        self.foreground= None
        self.x = x
        self.y = y
        
    def draw(self):
        self.background.draw()
        if self.element:
            self.element.draw()
        if self.foreground:
            self.foreground.draw()
            self.update()
    def update(self):
        pass

class Sand(Cell):

    images = [(pyglet.image.load('images/background/sand{}.png'.format(i)), weight)
              for (i, weight) in [(1, 90), (2, 10), (3,10), (4, 2), (5,2), (6,2)] ]

    def __init__(self, *args, **kwargs):
        self.images = Sand.images
        super(Sand, self).__init__(*args, **kwargs)


class Jungle(Cell):

    images = [(pyglet.image.load('images/background/jungle{}.png'.format(i)), weight)
              for (i, weight) in [(1, 1), (2, 1), (3,1), (4, 2), (5,2), (6,2)] ]

    def __init__(self, *args, **kwargs):
        self.images = Jungle.images
        super(Jungle, self).__init__(*args, **kwargs)

class Sea(Cell):
    
    images = [(pyglet.image.load('images/background/sea{}.png'.format(i)), weight)
              for (i, weight) in [(1, 90), (2, 10), (3,10), (4, 2), (5,2), (6,2)] ]

    def __init__(self, *args, **kwargs):
        super(Sea, self).__init__(*args, **kwargs)
        image_population = [image for (image, weight) in self.images for i in xrange(weight)]
        self.foreground = pyglet.sprite.Sprite(random.choice(image_population), self.x, self.y)

class SeaBorder(Cell):
    
    back_images = [(pyglet.image.load('images/background/sand{}.png'.format(i)), weight)
              for (i, weight) in [(1, 90), (2, 10), (3,10), (4, 2), (5,2), (6,2)] ]

    front_image = [pyglet.image.load('images/background/seaborder{}.png'.format(i))
              for i in xrange(1,4) ]

    def __init__(self, *args, **kwargs):
        self.tick=0
        self.images = SeaBorder.back_images
        super(SeaBorder, self).__init__(*args, **kwargs)
        self.foreground =  pyglet.sprite.Sprite(random.choice(SeaBorder.front_image),self.x,self.y)

    def update(self):
        self.tick += 1
        dx = (cos(self.tick/25.0)*config.CELL_SIZE/4-config.CELL_SIZE/4)*0.3
        self.foreground = pyglet.sprite.Sprite(self.foreground.image,self.x+dx,self.y)



if __name__ == '__main__':

    # drawing test
    window = pyglet.window.Window()
    seaBack = SeaBorder(x=window.width//4, y=window.height//4)
    
    @window.event
    def on_draw():
            window.clear()
            #sandBack = Sand(x=window.width//4, y=window.height//4)
            
            # jungleBack = Jungle(x=window.width//4, y=window.height//4)

            #sandBack.draw()
            seaBack.draw()
            # jungleBack.draw()

    pyglet.app.run()
