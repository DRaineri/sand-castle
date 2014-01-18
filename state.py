from math import cos, sin, ceil, pi

class State(object):
	"""docstring for State"""
	anim_delay = 0.1

	def __init__(self, element, anim_delay=anim_delay):
		self.t = 0
		self.element = element	
		self.anim_delay = anim_delay

	def update(self, dt):
		self.t += dt

		frame_id = int(self.t / self.anim_delay) % len(self.images)

		images_frame = self.images[frame_id]

		pos_angle = (self.element.angle + pi / 4 + 2 * pi) % (2 * pi)
		angle_fragment = int(len(images_frame) * (pos_angle / (2 * pi))) 

		self.element.cur_image = images_frame[angle_fragment]	

class Idle(State):
	"""docstring for Idle"""
	def __init__(self, element):
		super(Idle, self).__init__(element)
		self.images = self.element.images[Idle]


	def update(self, dt):
		super(Idle, self).update(dt)

class Moving(State):
	"""docstring for Moving"""

	def __init__(self, element, offset):
		super(Moving, self).__init__(element)
		self.offset = offset	
		self.images = self.element.images[Moving]

	def update(self, dt):
		super(Moving,self).update(dt)

		angle = self.element.angle + self.offset
		distancePix = self.element.speed * dt
		self.element.x += distancePix * cos(angle)
		self.element.y += distancePix * sin(angle)

	#def interact():
	#	print "interact"



	

class Attacking(State):
	"""docstring for Attacking"""
	def __init__(self, arg):
		super(Attacking, self).__init__()
		self.images = self.element.images[Attacking]

	def update(self, dt):
		super(Attacking,self).update(dt)

