#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from state import Idle, Moving, Attacking,Dying
import config
from math import cos 

from math import radians, atan2

class Element(object):
    """ Main class of elements on board """
    def __init__(self, game, x, y, w=1, h=1):
        super(Element, self).__init__()
        self.x, self.y = x, y
        self.w, self.h = w, h

        self.game = game
        
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

    def center(self):
        center = (self.x + self.w*config.CELL_SIZE/2 , self.y + self.h*config.CELL_SIZE/2)
        return center

    def diff_angle(self, element):
        e_x, e_y = element.center()
        return atan2(e_y - self.y , e_x -self.x)

    def draw(self):
        sprite = pyglet.sprite.Sprite(self.cur_image, self.x, self.y)
        sprite.draw()

    def interact(self, character):
        pass

    def collision(self):
        self.state = Idle(self)

    def cells(self):
        cell_x = int(self.x // config.CELL_SIZE)
        cell_y = int(self.y // config.CELL_SIZE)

        return [(cell_x + i, cell_y + j) for i in xrange(self.w) for j in xrange(self.h)
                if 0 <= cell_x + i < self.game.grid.w and 0 <= cell_y + j < self.game.grid.h ]

    def is_collidable(self):
        return True


#SubClass
class Creature(Element):

    def __init__(self, *args, **kwargs):
        super(Creature, self).__init__(*args, **kwargs)
        self.hp = 10
        self.target = None
        self.angle = 0.0
        self.speed = 500

    def attack_finished(self):
        for n in self.game.grid.neighbours(self):
            self.attack(n)

        self.state = Idle(self)

    def attack(self, element):
        element.hp -= self.att
        if element.hp <= 0:
            element.state = Dying(element)

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
			],
			Dying : [
			[pyglet.image.load('images/char/dying/0_{}.png'.format(p)) for p in ['death']]
			],
			Attacking : [
			[pyglet.image.load('images/char/attacking/{}_{}.png'.format(f,p)) for p in ['right', 'left','bottom'] for f in range(4) 
			],[pyglet.image.load('images/char/attacking/{}_top.png'.format(f))  for f in range(2)]
			]
			 }

	def __init__(self, *args, **kwargs):
		self.hp = 20
		self.att = 5
		self.images = Character.images

		super(Character, self).__init__(*args, w=1, h=2, **kwargs)



class Castle(Creature):
    images = {

            Idle: [
            [pyglet.image.load('images/castle/idle/{}.png'.format(pos)) for pos in ['etat0', 'etat1', 'etat2']]
            ],
            Dying : [
            [pyglet.image.load('images/char/dying/0_{}.png'.format(p)) for p in ['death']]
            ],
             }
    def __init__(self, *args, **kwargs):
        self.images = Castle.images
        self.att=5
        self.hp = 100
        super(Castle, self).__init__(*args, **kwargs)

<<<<<<< HEAD
	def interact(self, character):
		print "magicCastle !!!"
		self.game.launch_crafting()
=======
    def interact(self, character):
        print "magicCastle !!!"
        self.game.launch_crafting()
        pass
>>>>>>> 6451231fd0bcbd06ac9783a09948ac7b605417e3



class Monster(Creature):
    images = None


    def attack_finished(self):
        super(Monster, self).attack_finished()

        for n in self.game.grid.neighbours(self):
            if isinstance(n, Character) or isinstance(n, Castle):
                self.state = Attacking(self)
                return

        self.state = Moving(self, self.getAngle())

    def getAngle(self):
        c_x, c_y = self.game.castle.x, self.game.castle.y
        offset = atan2(c_y - self.y , c_x -self.x)
        return offset

    def __init__(self, *args, **kwargs):
        
        self.hp = 30
        self.att = 2

        super(Monster, self).__init__(*args, **kwargs)
        self.speed = 100

    def collision(self):
        neighbours = self.game.grid.neighbours(self)
        for n in neighbours:
            if isinstance(n, Castle) or isinstance(n, Character):
                self.state = Attacking(self,n)
                return

class SeaMonster(Monster):
    images = {

            Idle: [
            [pyglet.image.load('images/monster/seamonster/idle/0_right.png')]
            ],
            Moving : [
            [pyglet.image.load('images/monster/seamonster/moving/{}_right.png'.format(f))] for f in range(4) 
            ],
            Attacking : [
            [pyglet.image.load('images/monster/seamonster/attacking/{}_{}.png'.format(f,p)) for p in ['right']] for f in range(4) 
            ],
            Dying : [
            [pyglet.image.load('images/monster/seamonster/dying/0_{}.png'.format(p)) for p in ['death']]
            ],
            
             }

    def __init__(self, *args, **kwargs):
        self.images = SeaMonster.images
        super(SeaMonster,self).__init__(*args,**kwargs)

class JungleMonster(Monster):
    images = {

            Idle: [
            [pyglet.image.load('images/monster/junglemonster/idle/0_left.png')]
            ],
            Moving : [
            [pyglet.image.load('images/monster/junglemonster/moving/{}_left.png'.format(f))] for f in range(4) 
            ],
            Attacking : [
            [pyglet.image.load('images/monster/junglemonster/attacking/{}_{}.png'.format(f,p)) for p in ['left']] for f in range(4) 
            ],
            Dying : [
            [pyglet.image.load('images/monster/junglemonster/dying/0_{}.png'.format(p)) for p in ['death']]
            ],
            
             }

    def __init__(self, *args, **kwargs):
        self.images = JungleMonster.images
        super(JungleMonster,self).__init__(*args,**kwargs)


class Chest(StillObject):
    images = {

            Idle: [
            [pyglet.image.load('images/chest/idle/chest_idle.png')]
            ]
             }

    def __init__(self, *args, **kwargs):
        self.images = Chest.images
        super(Chest, self).__init__(*args, **kwargs)
        self.angle = 0.0
    
    def interact(self, character):
        character.game.ruby += 1

class Projectile(Creature):
    images = {

            Idle: [
            [pyglet.image.load('images/projectile/idle/bomb.png')]
            ],
            Moving: [
            [pyglet.image.load('images/projectile/idle/bomb.png')]
            ]
    }

    def __init__(self, *args, **kwargs):
        self.images = Projectile.images
        super(Projectile, self).__init__(*args, **kwargs)

    def shoot(self, target):
        angle = self.diff_angle(target)
        self.state = Moving(self, angle)

    def collision(self):
        pass
    
    def is_collidable(self):
        return False


class Foam(StillObject):
    images = {

            Idle: [
            [pyglet.image.load('images/foam/idle/idle.png')]
            ]
             }

    def __init__(self, *args, **kwargs):
        self.images = Foam.images
        super(Foam, self).__init__(*args, **kwargs)
        self.angle = 0.0
        self.x0 = self.x
        self.tick=0


    def update(self, dt):
        super(Foam,self).update(dt)
        self.tick += 1
        dx = (cos(self.tick/25.0)*config.CELL_SIZE/4-config.CELL_SIZE/4)*0.3
        self.x = self.x0 - dx
        
if __name__ == '__main__':
    pass
