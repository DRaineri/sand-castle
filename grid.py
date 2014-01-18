import random

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

