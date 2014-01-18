import random
import config
import pyglet

def random_bg():
	return random.choice([Sand, Jungle, Sea])

class Grid(object):
	def __init__(self, w, h):
		self.grid = [[ None for x in xrange(w)] for y in xrange(h)]
		self.random_populate()
		self.w=w
		self.h=h
		print self.h, self.w

	def random_populate(self):
		for y, row in enumerate(self.grid):
			for x, col in enumerate(row):
				r_x, r_y = x * config.CELL_SIZE, y * config.CELL_SIZE
				bg = Sand(r_x, r_y)
				self.grid[y][x] = Cell(bg)

	def draw_background(self):
		for row in self.grid:
			for cell in row:
				cell.draw()

	def neighbours(self, element):
		neigh = []
		b_x = element.x // config.CELL_SIZE - 1
		b_y = element.y // config.CELL_SIZE - 1

		for x in xrange(b_x, b_x + element.w + 1):
			for y in xrange(b_y, b_y + element.h + 1):
				if 0 <= x < self.w and 0 <= y < self.h and self.grid[y][x].element and self.grid[y][x].element != element:
					neigh.append(self.grid[y][x].element)

		return neigh

	def update_elements(self, elements):
		for element in elements:
			for x, y in element.cells():
				self.grid[y][x].element = element

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

²	def __init__(self, x, y):
		super(Background, self).__init__()

		image_population = [image  for (image, weight) in self.images for i in xrange(weight)]
		self.sprite = pyglet.sprite.Sprite(random.choice(image_population), x, y)
	
	def draw(self):
		self.sprite.draw()

class Sand(Background):

	images = [(pyglet.image.load('images/background/sand{}.png'.format(i)), weight)
	          for (i, weight) in [(1, 90), (2, 10), (3,10), (4, 2), (5,2), (6,2)] ]

	def __init__(self, *args, **kwargs):
		self.images = Sand.images
		super(Sand, self).__init__(*args, **kwargs)


class Jungle(Background):

	images = [pyglet.image.load('images/background/{}.png'.format(pos)) for pos in ['jungle1', 'jungle2', 'jungle3']]

	def __init__(self, *args, **kwargs):
		self.images = Jungle.images
		super(Jungle, self).__init__(*args, **kwargs)

class Sea(Background):
	
	images = [pyglet.image.load('images/background/{}.png'.format(pos)) for pos in ['sea1', 'sea2', 'sea3']]

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
