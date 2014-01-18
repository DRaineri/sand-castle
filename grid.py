import random
import pyglet

class Background(object):
	"""Class that generate a background object"""
	
	images = list()

	def __init__(self, x, y):
		super(Background, self).__init__()
		self.sprite = pyglet.sprite.Sprite(random.choice(self.images), x, y)
	
	def draw(self):
		self.sprite.draw()

class Sand(Background):
	image1 = pyglet.image.load('Images/Background/sand1.png')
	image2 = pyglet.image.load('Images/Background/sand2.png')
	image3 = pyglet.image.load('Images/Background/sand3.png')
	image4 = pyglet.image.load('Images/Background/sand4.png')
	image5 = pyglet.image.load('Images/Background/sand5.png')

	images = [image1, image2, image3, image4, image5]

	def __init__(self, *args, **kwargs):
		self.images = Sand.images
		super(Sand, self).__init__(*args, **kwargs)


class Jungle(Background):
	image1 = pyglet.image.load('Images/Background/jungle1.png')
	image2 = pyglet.image.load('Images/Background/jungle2.png')
	image3 = pyglet.image.load('Images/Background/jungle3.png')
	image4 = pyglet.image.load('Images/Background/jungle4.png')
	image5 = pyglet.image.load('Images/Background/jungle5.png')

	images = [image1, image2, image3, image4, image5]

	def __init__(self, *args, **kwargs):
		self.images = Jungle.images
		super(Jungle, self).__init__(*args, **kwargs)

class Sea(Background):
	image1 = pyglet.image.load('Images/Background/sea1.png')
	image2 = pyglet.image.load('Images/Background/sea2.png')
	image3 = pyglet.image.load('Images/Background/sea3.png')
	image4 = pyglet.image.load('Images/Background/sea4.png')
	image5 = pyglet.image.load('Images/Background/sea5.png')

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

