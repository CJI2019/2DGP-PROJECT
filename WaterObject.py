from pico2d import *

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600

class WATER:
    def __init__(self):
        self.image = load_image('Water_alpha.png')
        self.x = GameWindow_WITDH//2
        self.y = -self.image.h+300-500
        self.speed = 0.5
    def drawAupdate(self):
        self.image.draw(self.x,self.y)
        self.y += self.speed
    def Crash(self,Player):
        if(self.y+self.image.h//2 > Player.y1):
            self.y -= self.speed

        