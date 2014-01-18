class Item(object):
	"""Class implementing a ressource, which is used tu build improvement for the castle"""
	
	name = '';
	icon = '';

	def __init__(self):
		super(Ressource, self).__init__()
		self.Value = value;		

#Subclasses
class SharkLeather(Ressource):
	"""First type of ressource, dropped on sea monster"""
	
	name = 'SharkLeather'
#	icon = pyglet.image.load('images/ressources/sharkleather.png')
	
	def __init__(self):
		super(SharkLeather, self).__init__()
		

class Ruby(Ressource):
	"""Third type of ressource, taken in chest"""
	name = 'Ruby'
#	icon = pyglet.image.load('images/ressources/ruby.png')
	def __init__(self):
			super(Ruby, self).__init__()
		
		


		

if __name__ == '__main__':
	pass