#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet

class GameWindow(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super(GameWindow, self).__init__(*args, **kwargs)

		# Background
		self.background_image = pyglet.image.SolidColorImagePattern(color=(20, 20, 50, 255)).create_image(800, 600)
		self.background = pyglet.sprite.Sprite(self.background_image)

		# Title
		self.title = pyglet.text.Label(text="Game title", font_name="Ubuntu", bold=True, font_size=18, x=400, y=565, anchor_x='center')
		# self.game = Game()

		# Setting an update frequency of 60hz
		pyglet.clock.schedule_interval(self.update, 1.0 / 60)

		# Graphical objects in the background (ordered by layer)
		self.background_objects = []

	def update(self, dt):
		pass

	def on_draw(self):
		pass

	def on_mouse_motion(self, x, y, dx, dy):
		pass

	def on_mouse_press(self, x, y):
		print x, y

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
	
	g = GameWindow(800, 600)

	# Running the app
	pyglet.app.run()
