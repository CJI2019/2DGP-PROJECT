from pico2d import *

import game_framework as gf
import Game_title

class POTAL:
    def __init__(self,x,y):
        self.image = load_image('Potal.png')
        self.frame = 0
        self.x = x
        self.y = y
    def draw(self):
        if self.frame < 5:
            self.image.clip_composite_draw(int(self.frame) * self.image.w//5,self.image.h//2,self.image.w//5,self.image.h//2,0,'',self.x,self.y,100,100)
        else:
            self.image.clip_composite_draw((int(self.frame)-5) * self.image.w//5,0,self.image.w//5,self.image.h//2,0,'',self.x,self.y,100,100)
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * gf.frame_time) % FRAMES_PER_ACTION

    def floorchange(self, FloorLevelAnimeCount, FloorLevelAnimeSpeed):
        if FloorLevelAnimeCount > 0:
            self.y += FloorLevelAnimeSpeed
        else:
            self.y -= FloorLevelAnimeSpeed
    def collision(self,a): # 플레이어 정점과 충돌
        la, ta, ra, ba = self.get_bb()
        lb, tb, rb, bb = a.get_bb()
        if la > rb: return
        if ra < lb: return
        if ta < bb: return
        if ba > tb: return

        if Game_title.Button.NORMAL == 0:
            Game_title.Button.NORMAL = 1
        else:
            Game_title.Button.HARD = 1
        import game_next_level
        gf.push_state(game_next_level)
    def get_bb(self):
        return self.x - 30 , self.y + 30 , self.x + 30 ,self.y - 30
ACTION_PER_TIME = 1.0 / 0.7
FRAMES_PER_ACTION = 8