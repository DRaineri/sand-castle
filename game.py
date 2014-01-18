#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from grid import Grid
from elements import Character
from math import atan2
import config

class GameWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super(GameWindow, self).__init__(*args, **kwargs)

		self.width, self.height = args[:2]

		# Background
		bg_color = pyglet.image.SolidColorImagePattern(color=(20, 20, 50, 255))
		self.background_image = bg_color.create_image(self.width, self.height)
		self.background = pyglet.sprite.Sprite(self.background_image)

		self.grid = Grid(20, 10)

		# Title
		t_x = self.width / 2
		t_y = self.height - 20
		self.title = pyglet.text.Label(text="Game title", font_name="Ubuntu", bold=True, font_size=28,
			                           x=t_x, y=t_y, anchor_x='center', anchor_y='top')

		# Graphical objects
		self.elements = []

		self.character = Character('Main Character', 10, 0, 0)

		# Setting an update frequency of 60hz
		pyglet.clock.schedule_interval(self.update, 1.0 / 60)


	def update(self, dt):
		self.character.update(dt)

		for element in self.elements:
			element.update(dt)

	def on_draw(self):
		self.background.draw()
		self.grid.draw_background()
		self.title.draw()

		self.character.draw()

		for element in self.elements:
			element.draw()

	def on_mouse_motion(self, x, y, dx, dy):
		c_x = self.character.x + self.character.w * config.CELL_SIZE / 2.0
		c_y = self.character.y + self.character.h * config.CELL_SIZE / 2.0
		self.character.angle = atan2(y - c_y, x - c_x)

	def on_mouse_press(self, x, y, button, modifiers):
		pass

	def on_key_press(self, symbol, modifiers):
		x_diff = 0
		y_diff = 0
		diff = 40

		if symbol == pyglet.window.key.UP:
			self.character.y += diff
			y_diff = 25
		elif symbol == pyglet.window.key.DOWN:
			self.character.y -= diff
			y_diff = -25
		elif symbol == pyglet.window.key.RIGHT:
			self.character.x += diff
			x_diff = 25
		elif symbol == pyglet.window.key.LEFT:
			self.character.x -= diff
			x_diff = -25

	def on_key_release(self, symbol, modifiers):
		if symbol in {pyglet.window.key.UP, pyglet.window.key.DOWN, pyglet.window.key.RIGHT, pyglet.window.key.LEFT}:
			pass#self.character.state = Idle()

if __name__ == '__main__':
	
	g = GameWindow(1024, 600)

	# Running the app
	pyglet.app.run()
