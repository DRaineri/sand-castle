import random
import config
import pyglet

from elements import Character

def random_bg():
	return random.choice([Sand, Jungle, Sea])

class Grid(object):
	def __init__(self, w, h):
		self.grid = [[ None for x in xrange(w)] for y in xrange(h)]
		self.random_populate()

		self.w = w
		self.h = h


	def random_populate(self):
		for y, row in enumerate(self.grid):
			for x, col in enumerate(row):
				r_x, r_y = x * config.CELL_SIZE, y * config.CELL_SIZE
				self.grid[y][x] =Sand(r_x, r_y)

	def draw_background(self):
		for row in self.grid:
			for cell in row:
				cell.background.draw()

	def draw_foreground(self):
		for row in self.grid:
			for cell in row:
				cell.foreground.draw()

	def neighbours(self, element):
		neigh = []
		b_x = int(element.x // config.CELL_SIZE) - 1
		b_y = int(element.y // config.CELL_SIZE) - 1

		for x in xrange(b_x, b_x + element.w + 2):
			for y in xrange(b_y, b_y + element.h + 2):
				el = self.grid[y][x].element
				valid_coords = 0 <= x < self.w and 0 <= y < self.h
				valid_neighbour = not el is None and el != element and not el in neigh
				if valid_coords and valid_neighbour:
					neigh.append(self.grid[y][x].element)

		return neigh

	def update_elements(self, elements):
		for row in self.grid:
			for cell in row:
				cell.element = None

		for element in elements:
			for x, y in element.cells():
				self.grid[y][x].element = element


class Cell(object):
	def __init__(self,x,y, element=None):
		self.element = element
		image_population = [image for (image, weight) in self.images for i in xrange(weight)]
		self.background = pyglet.sprite.Sprite(random.choice(image_population), x, y)
		self.foreground= None
		
	def draw(self):
		self.background.draw()
		if self.element:
			self.element.draw()
		if self.foreground:
			self.foreground.draw()

class Sand(Cell):

	images = [(pyglet.image.load('images/background/sand{}.png'.format(i)), weight)
	          for (i, weight) in [(1, 90), (2, 10), (3,10), (4, 2), (5,2), (6,2)] ]

	def __init__(self, *args, **kwargs):
		self.images = Sand.images
		super(Sand, self).__init__(*args, **kwargs)


class Jungle(Cell):

	images = [pyglet.image.load('images/background/{}.png'.format(pos)) for pos in ['jungle1', 'jungle2', 'jungle3']]

	def __init__(self, *args, **kwargs):
		self.images = Jungle.images
		super(Jungle, self).__init__(*args, **kwargs)

class Sea(Cell):
	
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
