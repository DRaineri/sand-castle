class Element(object):
	""" Main class of elements on board """
	def __init__(self, posX, posY, sizeX, sizeY):
		super(Element, self).__init__()
		self.pos = (posX, posY)
		self.size = (sizeX, sizeY)
		self.state = Idle()

class Creature(Element):
	def __init__(self):
		super(Monster, self).__init__()
		this.angle = 0;

class StillObject(Element):
	def __init__(self):
		super(ClassName, self).__init__()
		
class Character(Creature):
	def __init__(self, name):
		self.name = name

class Castle(Creature):
	def __init__(self, arg):
		super(Castle,Creature.__init__()
		self.arg = arg
		
class Monster(Creature):
	def __init__(self, arg):
		super(Monster, self).__init__()
		self.arg = arg
		