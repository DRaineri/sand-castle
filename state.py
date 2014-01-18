import math

class State(object):
	"""docstring for State"""
	def __init__(self, element):
		self.t = 0
		self.element = element		

	def update(self, dt):
		self.t += dt

	

class Idle(State):
	"""docstring for Idle"""
	def __init__(self, arg):
		super(Idle, self).__init__()
		self.arg = arg

	def update(self, dt):
		self.time_passed += dt

class Moving(State):
	"""docstring for Moving"""

	anim_delay = 0.2
	def __init__(self, element, anim_delay=anim_delay):
		super(Moving, self).__init__(element)
		self.anim_delay = anim_delay


	def update(self, dt):
		super(Moving,self).update(dt)
		self.time_passed += dt

		angle = self.element
		distancePix = self.element.speed*dt
		self.element.pos.posX = distancePix*cos(angle)
		self.element.pos.posY = distancePix*sin(angle)

		if (self.time_passed > self.anim_delay):	
			imagesMoving = self.element.images[Moving]
			imagesFrame = imagesMoving[(self.t / self.anim_delay) % len(self.element.images)]
			self.element.cur_image=imagesFrame[ceil(angle/(2*PI)*len(imagesFrame))]	

			self.time_passed = 0



		
 #
 #class Attacking(State):
 #	"""docstring for Attacking"""
 #	def __init__(self, arg):
 #		super(Attacking, self).__init__()
 #		self.arg = arg
 #
 #	def 
 #
 #
 #class Idle(State):
 #	"""docstring for Iddle"""
 #	def __init__(self, arg):
 #		super(Iddle, self).__init__()
 #		self.arg = arg
 #		
 #class Openning(State):
 #	"""docstring for Openning"""
 #	def __init__(self, arg):
 #		super(Openning, self).__init__()
 #		self.arg = arg
 #