from pico2d import *

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600

class WATER:
    def __init__(self):
        self.image = load_image('Water_alpha2.png')
        self.face = load_image('Wateranime_alpha.png')

        self.x = GameWindow_WITDH//2
        self.y = -self.image.h+300-500
        self.speed = 2
        self.facespeed ,self.faceXpos= 5 , GameWindow_WITDH//2
    def draw(self):
        self.image.draw(self.x,self.y)
        self.face.draw(self.faceXpos,self.y + self.image.h//2 - self.face.h//2)
        self.face.draw(self.faceXpos - 700 -GameWindow_WITDH//2,self.y + self.image.h//2 - self.face.h//2)

    def update(self):
        self.y += self.speed
        self.faceXpos += self.facespeed
        if self.faceXpos >= 1200:
            self.faceXpos = GameWindow_WITDH // 2
    def Crash(self,Player):
        if(self.y+self.image.h//2 > Player.y1):
            self.y -= self.speed

        