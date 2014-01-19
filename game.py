#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from grid import Grid




from elements import Character, Monster, Castle, Chest, Projectile, Foam, SeaMonster, JungleMonster



from pyglet.window import key

from crafting import Screen_craft

import config
import random
from state import Moving, Idle, Attacking,Dying
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
        self.shark_teeth = 0
        self.bear_teeth = 0 

        # Background
        bg_color = pyglet.image.SolidColorImagePattern(color=(20, 20, 50, 255))
        self.background_image = bg_color.create_image(self.width, self.height)
        self.background = pyglet.sprite.Sprite(self.background_image)

        g_w, g_h = self.width // config.CELL_SIZE + 1, self.height // config.CELL_SIZE + 1
        self.grid = Grid(g_w, g_h)

        # Graphical objects
        self.elements = []

        self.character = Character(self, (self.width)/2-(3*config.CELL_SIZE)-10, (self.height)/2-10)
        self.castle = Castle(self,(self.width)/2-(1.5*config.CELL_SIZE), (self.height)/2, 2,2)
        
        self.foam = Foam(self,-50,-300)

        self.elements.append(self.character)

        self.addSeaMonster()
        self.addSeaMonster()
        self.addJungleMonster()


        self.elements.append(Chest(self,750,0))




        self.screen_craft = Screen_craft(self)

        self.elements.append(self.castle)
    

        self.crafting_on = False


        # Setting an update frequency of 60hz
        pyglet.clock.schedule_interval(self.update, 1.0 / 60)
        pyglet.clock.schedule_interval(self.addSeaMonster, 5)
        pyglet.clock.schedule_interval(self.addJungleMonster, 5)

        pyglet.clock.schedule_interval(self.shoot_monsters, 2)

    def shoot_monsters(self, dt=0):
        monster = None
        for el in self.elements:
            if isinstance(el, Monster):
                monster = el
                break


        if not monster:
            return

        proj = Projectile(self, self.castle.x, self.castle.y)
        proj.shoot(monster)
        self.elements.append(proj)

    def addSeaMonster(self, dt=0):
        sea_monster = SeaMonster(self, 0, random.randint(0,self.height), 2, 2)

        self.elements.append(sea_monster)
        offset=sea_monster.getAngle()
        sea_monster.state = Moving(sea_monster, offset)

    def addJungleMonster(self, dt=0):
        jungle_monster = JungleMonster(self, self.width, random.randint(0,self.height), 2, 2)

        self.elements.append(jungle_monster)
        offset=jungle_monster.getAngle()
        jungle_monster.state = Moving(jungle_monster, offset)

    def update(self, dt):
        for element in self.elements:
            element.update(dt)
        # Updating the element in grids
        self.grid.update_elements(self.elements)
        self.foam.update(dt)

    def on_draw(self):
        self.background.draw()
        self.grid.draw_background()


        # Drawing all elements
        for element in self.elements:
            element.draw()
        
        self.grid.draw_foreground()
        self.foam.draw()

        # Title
        t_x = self.width - 20
        t_y = self.height - 10
        header_text = "Rubies: {} - Shark Teeth: {} - Bear Teeth {}".format(self.ruby, self.shark_teeth, self.bear_teeth)
        header = pyglet.text.Label(text=header_text, font_name="Ubuntu", bold=False, font_size=16,
                                       x=t_x, y=t_y, anchor_x='right', anchor_y='top')
        header.draw()

        if self.crafting_on:
            self.screen_craft.draw()


    def on_mouse_motion(self, x, y, dx, dy): 
        self.update_angle(x, y)

    def update_angle(self, x, y):
        c_x = self.character.x + self.character.w * config.CELL_SIZE / 2.0
        c_y = self.character.y + self.character.h * config.CELL_SIZE / 2.0
        self.character.angle = atan2(y - c_y, x - c_x)



    def on_mouse_press(self, x, y, button, modifiers): 
        if button == pyglet.window.mouse.LEFT:
            neighboors = self.grid.neighbours(self.character)
            for el in neighboors:

                if (isinstance(el, SeaMonster)) or (isinstance(el, JungleMonster)):
                    # TODO : Change this by switching the state to attacking
                    self.character.attack(el)

                    return
        elif button == pyglet.window.mouse.RIGHT:
            cell = self.grid.grid[y/config.CELL_SIZE][x/config.CELL_SIZE]
            if cell.element and cell.element in self.grid.neighbours(self.character):
                cell.element.interact(self.character)

            #wait release

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        x_diff = 0
        y_diff = 0
        diff = 40
        offset = 0

        if symbol == pyglet.window.key.UP:
            offset= radians(90)
            self.character.state=Moving(self.character, offset)
        elif symbol == pyglet.window.key.DOWN:
            offset = radians(-90)
            self.character.state=Moving(self.character, offset)
        elif symbol == pyglet.window.key.RIGHT:
            offset = radians(0)
            self.character.state=Moving(self.character, offset)
        elif symbol == pyglet.window.key.LEFT:
            offset = radians(180)
            self.character.state=Moving(self.character, offset)
        elif symbol == pyglet.window.key.P:
            pyglet.clock.unschedule(self.update)
            pyglet.clock.unschedule(self.addSeaMonster)
            pyglet.clock.unschedule(self.addJungleMonster)
        elif symbol == pyglet.window.key.G:
            pyglet.clock.schedule_interval(self.update, 1.0 / 60)
            pyglet.clock.schedule_interval(self.addSeaMonster, 5)
            pyglet.clock.schedule_interval(self.addJungleMonster, 5)

        elif symbol == pyglet.window.key.Q:
            self.leave_crafting()

      




    def on_key_release(self, symbol, modifiers):
        movement_keys = {pyglet.window.key.UP, pyglet.window.key.DOWN, pyglet.window.key.RIGHT, pyglet.window.key.LEFT} 
        
        if symbol in movement_keys and not any(self.keys[s] for s in movement_keys):
            self.character.state = Idle(self.character)

    def launch_crafting(self):
        pyglet.clock.unschedule(self.update)
        pyglet.clock.unschedule(self.addSeaMonster)
        pyglet.clock.schedule_interval(self.addJungleMonster, 5)

        self.crafting_on = True
        self.screen_craft.run_crafting()

    def leave_crafting(self):
        self.crafting_on = False
        pyglet.clock.schedule_interval(self.update, 1.0 / 60)
        pyglet.clock.schedule_interval(self.addSeaMonster, 5)
        pyglet.clock.schedule_interval(self.addJungleMonster, 5)



if __name__ == '__main__':
    g = GameWindow(1600, 800)
    # music = pyglet.resource.media('test.mp3')
    # music.play()


    # Running the app
    pyglet.app.run()
