#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from grid import Grid

from elements import Character, Monster, Castle

from pyglet.window import key

import config
import random
from state import Moving, Idle, Attacking
from math import radians, atan2

class GameWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super(GameWindow, self).__init__(*args, **kwargs)

		self.width, self.height = args[:2]
		
		# Keys handlers
		self.keys = key.KeyStateHandler()
		self.push_handlers(self.keys)

		# Resources
		self.ruby = 0
		self.shark_leather = 0

		# Background
		bg_color = pyglet.image.SolidColorImagePattern(color=(20, 20, 50, 255))
		self.background_image = bg_color.create_image(self.width, self.height)
		self.background = pyglet.sprite.Sprite(self.background_image)

		g_w, g_h = self.width // config.CELL_SIZE + 1, self.height // config.CELL_SIZE + 1
		self.grid = Grid(g_w, g_h)

		# Graphical objects
		self.elements = []

		self.character = Character(self, 10, 0)
		self.castle = Castle(self,(self.width)/2-(1.5*config.CELL_SIZE), (self.height)/2, 3,3)
		
		
		self.elements.append(self.character)
		self.addSeaMonster()
		self.addSeaMonster()
		
			


		self.elements.append(self.castle)

		# Setting an update frequency of 60hz
		pyglet.clock.schedule_interval(self.update, 1.0 / 60)
		pyglet.clock.schedule_interval(self.addSeaMonster, 5)


	def addSeaMonster(self, dt=0):
		monster = Monster(self, 0, random.randint(0,self.height), 1, 2)

		self.elements.append(monster)
		monster.setAngle()

	def update(self, dt):
		for element in self.elements:
			element.update(dt)




		# Updating the element in grids
		self.grid.update_elements(self.elements)

	def on_draw(self):
		self.background.draw()
		self.grid.draw_background()

		# Drawing all elements
		for element in self.elements:
			element.draw()

		# Title
		t_x = self.width - 20
		t_y = self.height - 10
		header_text = "Rubies: {} - Shark Leather: {}".format(self.ruby, self.shark_leather)
		header = pyglet.text.Label(text=header_text, font_name="Ubuntu", bold=False, font_size=16,
			                           x=t_x, y=t_y, anchor_x='right', anchor_y='top')
		header.draw()


	def on_mouse_motion(self, x, y, dx, dy): 
		self.update_angle(x, y)

	def update_angle(self, x, y):
		c_x = self.character.x + self.character.w * config.CELL_SIZE / 2.0
		c_y = self.character.y + self.character.h * config.CELL_SIZE / 2.0
		self.character.angle = atan2(y - c_y, x - c_x)


	def on_mouse_press(self, x, y, button, modifiers):
		if button == pyglet.window.mouse.LEFT:
			self.character.attack()
		elif button == pyglet.window.mouse.RIGHT:
			pass
			#wait release

	def on_mouse_release(self, x, y, button, modifiers):
		pass

	def on_key_press(self, symbol, modifiers):
		x_diff = 0
		y_diff = 0
		diff = 40
		offset = 0

		if symbol == pyglet.window.key.UP:
			self.character.state=Moving(self.character, offset)
		elif symbol == pyglet.window.key.DOWN:
			offset = radians(180)
			self.character.state=Moving(self.character, offset)
		elif symbol == pyglet.window.key.RIGHT:
			offset = radians(-90)
			self.character.state=Moving(self.character, offset)
		elif symbol == pyglet.window.key.LEFT:
			offset = radians(90)
			self.character.state=Moving(self.character, offset)


	def on_key_release(self, symbol, modifiers):
		
		

		movement_keys = {pyglet.window.key.UP, pyglet.window.key.DOWN, pyglet.window.key.RIGHT, pyglet.window.key.LEFT} 
		
		if symbol in movement_keys and not any(self.keys[s] for s in movement_keys):

			self.character.state = Idle(self.character)

if __name__ == '__main__':
	
	g = GameWindow(1280, 800)
	music = pyglet.resource.media('test.mp3')
	music.play()

	# Running the app
	pyglet.app.run()
