#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from grid import Grid
from elements import Character, Castle
from pyglet.window import key

import config
from state import Moving, Idle
from math import radians, atan2

class GameWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super(GameWindow, self).__init__(*args, **kwargs)

		self.width, self.height = args[:2]
		
		self.keys = key.KeyStateHandler()
		self.push_handlers(self.keys)

		# Background
		bg_color = pyglet.image.SolidColorImagePattern(color=(20, 20, 50, 255))
		self.background_image = bg_color.create_image(self.width, self.height)
		self.background = pyglet.sprite.Sprite(self.background_image)

		self.grid = Grid(25, 15)

		# Title
		t_x = self.width / 2
		t_y = self.height - 20
		self.title = pyglet.text.Label(text="Game title", font_name="Ubuntu", bold=True, font_size=28,
			                           x=t_x, y=t_y, anchor_x='center', anchor_y='top')

		# Graphical objects
		self.elements = []

		self.character = Character('Main Character', 10, 0, 0)
		self.elements.append(self.character)

		self.castle= Castle('Main Castle',(self.grid.w/2)-2, (self.grid.h/2)+2, 4,4)

		# Setting an update frequency of 60hz
		pyglet.clock.schedule_interval(self.update, 1.0 / 60)


	def update(self, dt):

		for element in self.elements:
			element.update(dt)

	def on_draw(self):
		self.background.draw()
		self.grid.draw_background()
		self.title.draw()

		for element in self.elements:
			element.draw()

	def on_mouse_motion(self, x, y, dx, dy): 
		self.update_angle(x, y)

	def update_angle(self, x, y):
		c_x = self.character.x + self.character.w * config.CELL_SIZE / 2.0
		c_y = self.character.y + self.character.h * config.CELL_SIZE / 2.0
		self.character.angle = atan2(y - c_y, x - c_x)


	def on_mouse_press(self, x, y, button, modifiers):
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
	

	# Running the app
	pyglet.app.run()
