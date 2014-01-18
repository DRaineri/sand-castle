#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from grid import Grid

class GameWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super(GameWindow, self).__init__(*args, **kwargs)

		self.width, self.height = args[:2]

		# Background
		bg_color = pyglet.image.SolidColorImagePattern(color=(20, 20, 50, 255))
		self.background_image = bg_color.create_image(self.width, self.height)
		self.background = pyglet.sprite.Sprite(self.background_image)

		self.grid = Grid(100, 60)

		# Title
		t_x = self.width / 2
		t_y = self.height - 20
		self.title = pyglet.text.Label(text="Game title", font_name="Ubuntu", bold=True, font_size=28,
			                           x=t_x, y=t_y, anchor_x='center', anchor_y='top')

		# Graphical objects
		self.elements = []


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
		pass

	def on_mouse_press(self, x, y, button, modifiers):
		pass

	def on_key_press(self, symbol, modifiers):
		x_diff = 0
		y_diff = 0

		if symbol == pyglet.window.key.UP:
			y_diff = 25
		elif symbol == pyglet.window.key.DOWN:
			y_diff = -25
		elif symbol == pyglet.window.key.RIGHT:
			x_diff = 25
		elif symbol == pyglet.window.key.LEFT:
			x_diff = -25



if __name__ == '__main__':
	
	g = GameWindow(1024, 600)

	# Running the app
	pyglet.app.run()
