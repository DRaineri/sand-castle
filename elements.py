#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from state import Idle, Moving

class Element(object):
	""" Main class of elements on board """
	def __init__(self, x, y, w=1, h=1):
		super(Element, self).__init__()
		self.x, self.y = x, y
		self.w, self.h = w, h

		self.state = Idle(self)
		self.last_state = Idle(self)
		
		self.cur_image = self.images[Idle][0][0]

	def update(self, dt):
		self.state.update(dt)

	def draw(self):
		print self.x, self.y
		sprite = pyglet.sprite.Sprite(self.cur_image, self.x, self.y)
		sprite.draw()

	def interact(self,element):
		pass

#SubClass
class Creature(Element):
	def __init__(self, hp=10, *args, **kwargs):
		super(Creature, self).__init__(*args, **kwargs)
		self.hp = hp
		self.angle = 0.0
		self.speed = 500

class StillObject(Element):
	def __init__(self, *args, **kwargs):
		super(StillObject, self).__init__(*args, **kwargs)

#SubSubClass
class Character(Creature):
	images = {

			Idle: [
			[pyglet.image.load('images/char/idle/0_{}.png'.format(pos)) for pos in ['right', 'top', 'left', 'bottom']]
			],
			Moving : [
			[pyglet.image.load('images/char/moving/{}_{}.png'.format(f,p)) for p in ['right', 'top', 'left', 'bottom']] for f in range(4) 
			
			]	
			 }

	def __init__(self, name, *args, **kwargs):
		self.name = name
		self.images = Character.images

		super(Character, self).__init__(*args, **kwargs)

class Castle(Creature):
	images = {

			Idle: [
			[pyglet.image.load('images/castle/idle/{}.png'.format(pos)) for pos in ['etat0', 'etat1', 'etat2']]
			]
			 }
	def __init__(self, *args, **kwargs):
			super(Castle,self).__init__(*args, **kwargs)
		
class Monster(Creature):
	def __init__(self, arg):
		super(Monster, self).__init__()

class Chest(StillObject):
	images = {

			Idle: [
			[pyglet.image.load('images/chest/idle/chest_idle.png')]
			]

			 }
	def __init__(self, name, *args, **kwargs):
		self.name = name
		self.images = Chest.images

		super(Chest, self).__init__(*args, **kwargs)
		# TODO : define what is in the chest

	
if __name__ == '__main__':
	pass

