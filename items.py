class Item(object):
	"""Class implementing a ressource, which is used tu build improvement for the castle"""
	
	name = '';
	icon = '';

	def __init__(self):
		super(Ressource, self).__init__()
		self.Value = value;		

#Subclasses
class SharkTeeth(Item):
	"""First type of ressource, dropped on sea monster"""
	
	name = 'SharkTeeth'
#	icon = pyglet.image.load('images/ressources/SharkTeeth.png')
	
	def __init__(self):
		super(SharkTeeth, self).__init__()
		

class Ruby(Item):
	"""Third type of ressource, taken in chest"""
	name = 'Ruby'
#	icon = pyglet.image.load('images/ressources/ruby.png')
	def __init__(self):
			super(Ruby, self).__init__()
		
		
class BearTeeth(Item):
	"""Second type of ressource, drop on jungle monster"""
	name = 'BearTeeth'
#	icon = pyglet.image.load('images/ressources/ruby.png')
	def __init__(self):
			super(BearTeeth, self).__init__()
		

		

if __name__ == '__main__':
	pass