from math import cos, sin, ceil, pi

class State(object):
	"""docstring for State"""
	def __init__(self, element):
		self.t = 0
		self.element = element	

	def update(self, dt):
		self.t += dt
	

class Idle(State):
	"""docstring for Idle"""
	def __init__(self, element):
		super(Idle, self).__init__(element)

	def update(self, dt):
		super(Idle, self).update(dt)

class Moving(State):
	"""docstring for Moving"""

	anim_delay = 0.2
	def __init__(self, element, offset, anim_delay=anim_delay):
		super(Moving, self).__init__(element)
		self.anim_delay = anim_delay
		self.element.offset=offset	


	def update(self, dt):
		super(Moving,self).update(dt)

		angle = self.element.angle+self.element.offset
		distancePix = self.element.speed * dt
		self.element.x += distancePix * cos(angle)
		self.element.y += distancePix * sin(angle)

		if self.t > self.anim_delay:	
			imagesMoving = self.element.images[Idle]
			imagesFrame = imagesMoving[(int(self.t / self.anim_delay)) % len(self.element.images)]
			self.element.cur_image=imagesFrame[int(ceil(angle/(2*pi)*len(imagesFrame)))]	

			self.t = 0

	def interact():
		print "interact"



	

#class Attacking(State):
#	"""docstring for Attacking"""
#	def __init__(self, arg):
#		super(Attacking, self).__init__()
#		self.arg = arg
#
#	def update(self, dt):
#		super(Attacking,self).update(dt)
#
#		angle = self.element.angle+offset
#		distancePix = self.element.speed * dt
#		self.element.x += distancePix * cos(angle)
#		self.element.y += distancePix * sin(angle)
#
#		if self.t > self.anim_delay:	
#			imagesMoving = self.element.images[Attack]
#			imagesFrame = imagesMoving[(int(self.t / self.anim_delay)) % len(self.element.images)]
#			self.element.cur_image=imagesFrame[int(ceil(angle/(2*pi)*len(imagesFrame)))]	
#
#			self.t = 0
#
#