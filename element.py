from state import Idle, Running

class Element(object):
	""" Main class of elements on board """
	def __init__(self, posX, posY, sizeX, sizeY):
		super(Element, self).__init__()
		self.pos = (posX, posY)
		self.size = (sizeX, sizeY)
		self.state = Idle()

	def update(self, dt):
		self.state.update(dt)

	def draw(self):
		self.cur_image.draw()

#SubClass
class Creature(Element):
	def __init__(self, hp):
		super(Creature, self).__init__()
		this.hp = hp
		this.angle = 0

class StillObject(Element):
	def __init__(self):
		super(StillObject, self).__init__()

#SubSubClass
class Character(Creature):
	images = {Idle: [], Running: []}

	def __init__(self, name):
		super(Character, self).__init__()
		self.name = name

		self.images = Character.images

class Castle(Creature):
	def __init__(self):²
		super(Castle,self).__init__()
		
class Monster(Creature):
	def __init__(self, arg):
		super(Monster, self).__init__()

class Chest(StillObject):
	def __init__(self):
		super(Chest,self).__init__()
		# TODO : define what is in the chest

		