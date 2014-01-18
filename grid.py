import random
import config
import pyglet

def random_bg():
	return random.choice([Sand, Jungle, Sea])

class Grid(object):
	def __init__(self, w, h):
		self.grid = [[ None for x in xrange(w)] for y in xrange(h)]
		self.random_populate()

	def random_populate(self):
		for y, row in enumerate(self.grid):
			for x, col in enumerate(row):
				r_x, r_y = x * config.CELL_SIZE, y * config.CELL_SIZE
				bg = random_bg()(r_x, r_y)
				self.grid[y][x] = Cell(bg)

	def draw_background(self):
		for row in self.grid:
			for cell in row:
				cell.draw()


class Cell(object):
	def __init__(self, background, element=None):
		self.background = background
		self.element = element

	def draw(self):
		self.background.draw()
		if self.element:
			self.element.draw()

class Background(object):
	"""Class that generate a background object"""
	
	images = list()

	def __init__(self, x, y):
		super(Background, self).__init__()
		self.sprite = pyglet.sprite.Sprite(random.choice(self.images), x, y)
	
	def draw(self):
		self.sprite.draw()

class Sand(Background):
	image1 = pyglet.image.load('images/background/sand1.png')
	image2 = pyglet.image.load('images/background/sand2.png')
	image3 = pyglet.image.load('images/background/sand3.png')
	image4 = pyglet.image.load('images/background/sand4.png')
	image5 = pyglet.image.load('images/background/sand5.png')

	images = [image1, image2, image3, image4, image5]

	def __init__(self, *args, **kwargs):
		self.images = Sand.images
		super(Sand, self).__init__(*args, **kwargs)


class Jungle(Background):
	image1 = pyglet.image.load('images/background/jungle1.png')
	image2 = pyglet.image.load('images/background/jungle2.png')
	image3 = pyglet.image.load('images/background/jungle3.png')
	image4 = pyglet.image.load('images/background/jungle4.png')
	image5 = pyglet.image.load('images/background/jungle5.png')

	images = [image1, image2, image3, image4, image5]

	def __init__(self, *args, **kwargs):
		self.images = Jungle.images
		super(Jungle, self).__init__(*args, **kwargs)

class Sea(Background):
	image1 = pyglet.image.load('images/background/sea1.png')
	image2 = pyglet.image.load('images/background/sea2.png')
	image3 = pyglet.image.load('images/background/sea3.png')
	image4 = pyglet.image.load('images/background/sea4.png')
	image5 = pyglet.image.load('images/background/sea5.png')

	images = [image1, image2, image3, image4, image5]
 
	def __init__(self, *args, **kwargs):
		self.images = Sea.images
		super(Sea, self).__init__(*args, **kwargs)

if __name__ == '__main__':

	# drawing test
	window = pyglet.window.Window()
	@window.event
	def on_draw():
			window.clear()
			sandBack = Sand(x=window.width//4, y=window.height//4)
			# seaBack = Sea(x=window.width//4, y=window.height//4)
			# jungleBack = Jungle(x=window.width//4, y=window.height//4)

			sandBack.draw()
			# seaBack.draw()
			# jungleBack.draw()

	pyglet.app.run()

