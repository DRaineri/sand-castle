import random
import config

def random_bg():
	return random.choice([Sand])

class Grid(object):
	def __init__(self, w, h):
		self.grid = [[ None for x in xrange(w)] for y in xrange(h)]
		self.random_populate()

	def random_populate(self):
		for y, row in enumerate(self.grid):
			for x, col in enumerate(row):
				r_x, r_y = x * config.CELL_SIZE, y * config.CELL_SIZE
				self.grid[y][x] = Cell(background=Sand(r_x, r_y))

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
		super(GeneratedBackground, self).__init__()
		self.sprites = pyglet.sprites.Sprites(random.choice(self.images), x, y)
	
	def draw(self):
		self.sprite.draw()

class Sand(Background):
	
	
	images

	def __init__(self, *args, **kwargs):
		self.images = Sand.images

