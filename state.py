class State(object):
	"""docstring for State"""
	def __init__(self, arg):
			self.arg = arg
		
class Moving(State):
	"""docstring for Moving"""
	def __init__(self, ):
		super(Moving, self).__init__()
		

class Attacking(State):
	"""docstring for Attacking"""
	def __init__(self, arg):
		super(Attacking, self).__init__()
		self.arg = arg


class Iddle(State):
	"""docstring for Iddle"""
	def __init__(self, arg):
		super(Iddle, self).__init__()
		self.arg = arg
		
class Openning(State):
	"""docstring for Openning"""
	def __init__(self, arg):
		super(Openning, self).__init__()
		self.arg = arg
