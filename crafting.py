import pyglet
import config

class SubCraft(object):
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.subList=[]

    def get_object(self, x,y):
        index=(int((self.y-y)/config.CRAFT_ICON_SIZE))
        if len(self.subList) < index-1 :
            return self.subList[index]
        return None


    def get_left_point(self,position):
        pos_x,pos_y = self.x+10, self.y+config.CRAFT_ICON_SIZE*position +20
        if pos_y<=self.y+self.h and position >= 0:
            return pos_x,pos_y
        return -1,-1



class ScreenCraft(object):
    """docstring for ScreenCraft"""
    def __init__(self, game):
        super(ScreenCraft, self).__init__()
        self.game = game
        self.background_image = pyglet.image.load("./images/crafting/background_crafting.png")
        self.pos_x_crafting = self.game.width/2 - self.background_image.width/2
        self.pos_y_crafting =  self.game.height/2 - self.background_image.height/2
        self.inventory=SubCraft(self.pos_x_crafting,self.pos_y_crafting,config.CRAFT_ICON_SIZE,self.background_image.height)

        pos_x_constructable=self.pos_x_crafting+self.background_image.width-config.CRAFT_ICON_SIZE
        self.constructable=SubCraft(pos_x_constructable,self.pos_y_crafting,config.CRAFT_ICON_SIZE,self.background_image.height)

    def get_sub_craft(self,x,y):
        if y> pos_y_crafting and y< pos_y_crafting+self.background_image.height:
            if x>=self.pos_x_crafting and x< pos_x_crafting+config.CRAFT_ICON_SIZE:
                return self.inventory
            elif x>self.background_image.width+self.pos_x_crafting-config.CRAFT_ICON_SIZE and x< self.background_image.width:
                return self.constructable
        return None

    def run_crafting(self):

        self.background = pyglet.sprite.Sprite(self.background_image, self.pos_x_crafting,self.pos_y_crafting)

        pos_x_symbole = self.game.width/2 - self.background_image.width/2 + 20
        pos_x_text = self.game.width/2 - self.background_image.width/2 + 440
        pos_y_symbole = self.game.height/2 - self.background_image.height/2 + 20
        pos_y_text = self.game.height/2 - self.background_image.height/2 + 60


        self.ruby_image = pyglet.image.load("./images/crafting/ruby.png")
        #self.ruby = pyglet.sprite.Sprite(self.ruby_image, pos_x_symbole, pos_y_symbole)
        lx,ly= self.inventory.get_left_point(0)
        self.ruby = pyglet.sprite.Sprite(self.ruby_image, lx,ly)
        self.inventory.subList.append(self.ruby)

        self.definition_1 = pyglet.text.Label(text="Evoluer le chateau", font_name="Ubuntu", bold=True, font_size=24,
                                       x=pos_x_text, y=pos_y_text, anchor_x='right', anchor_y='top')
    
    def draw(self):
        self.background.draw()
        self.ruby.draw()
        self.definition_1.draw()

    #def craft(self, x, y):
       # if pos_x_symbole <= x <= pos_x_symbole + self.ruby_image.width

