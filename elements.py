#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from state import Idle, Moving, Attacking
import config

class Element(object):
	""" Main class of elements on board """
	def __init__(self, x, y, w=1, h=1):
		super(Element, self).__init__()
		self.x, self.y = x, y
		self.w, self.h = w, h
		
		self._state = Idle(self)

		self.last_state = Idle(self)
		
		self.cur_image = self.images[Idle][0][0]

	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, value):
		self.last_state = self._state
		self._state = value

	def update(self, dt):
		self.state.update(dt)

	def draw(self):
		print self.x, self.y
		sprite = pyglet.sprite.Sprite(self.cur_image, self.x, self.y)
		sprite.draw()

	def interact(self,element):
		pass

	def cells(self):
		cell_x = self.x//config.CELL_SIZE
		cell_y = self.y//config.CELL_SIZE

		return [(cell_x + i, cell_y + j) for i in xrange(self.w) for j in xrange(self.h)]
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

	def attack(self):
		#liste des cases du character
		allPosCharacter = [(self.x//config.CELL_SIZE, self.y//config.CELL_SIZE),
							 ((self.x + self.w)//config.CELL_SIZE, self.y//config.CELL_SIZE),
							 (self.x //config.CELL_SIZE,(self.y + self.h)//config.CELL_SIZE),
							 ((self.x + self.w)//config.CELL_SIZE,(self.y + self.h)//config.CELL_SIZE)]
		allPosTarget = []
		for i in range(self.x//config.CELL_SIZE - 1, self.x//config.CELL_SIZE + 2):
			for j in range (self.y//config.CELL_SIZE - 1, self.y//config.CELL_SIZE + 2):
				if not((i,j) in allPosCharacter):
					allPosTarget.append((i,j))


		posElement = (x/config.CELL_SIZE, y/config.CELL_SIZE)

		self.state = Attacking(self)


class Castle(Creature):
	images = {

			Idle: [
			[pyglet.image.load('images/castle/idle/{}.png'.format(pos)) for pos in ['etat0', 'etat1', 'etat2']]
			]
			 }
	def __init__(self, *args, **kwargs):
			super(Castle,self).__init__(*args, **kwargs)
		
class Monster(Creature):
	images = {

			Idle: [
			[pyglet.image.load('images/monster/idle/0_right.png')]
			],
			Moving : [
			[pyglet.image.load('images/monster/moving/{}_right.png'.format(f)) for f in range(4)] 
			
			]
			
			 }

	def __init__(self, name, *args, **kwargs):
		self.name = name
		self.images = Monster.images

		super(Monster, self).__init__(*args, **kwargs)


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

