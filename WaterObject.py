from pico2d import *

import game_framework
import Main

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600
INF = 10000000
class WATER:
    def __init__(self):
        self.image = load_image('Water_alpha2.png')
        self.face = load_image('Wateranime_alpha.png')

        self.x = GameWindow_WITDH//2
        self.y = -self.image.h+300-500
        self.speed = 0.5 # speed 가 0이 되면 게임이 오버 된것이다.
        self.facespeed ,self.faceXpos= 2 , GameWindow_WITDH//2
    def draw(self):
        self.image.draw(self.x,self.y)
        self.face.draw(self.faceXpos,self.y + self.image.h//2 - self.face.h//2)
        self.face.draw(self.faceXpos - 700 -GameWindow_WITDH//2,self.y + self.image.h//2 - self.face.h//2)
    def update(self):
        global INF

        # return # maptool

        self.Crash()

        if Main.Skill.skill_state[0] == None :
            self.y += self.speed
            self.faceXpos += self.facespeed
            if self.faceXpos >= 1200:
                self.faceXpos = GameWindow_WITDH // 2
        self.y = clamp(-INF,self.y,400)

    def Crash(self):
        if(self.y+self.image.h//2 > Main.Player.y1):
            self.speed = 0
            import game_over_menu
            game_framework.push_state(game_over_menu)


        