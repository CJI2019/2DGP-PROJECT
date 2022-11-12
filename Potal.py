from pico2d import *

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
    def update(self,frame_time):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time) % FRAMES_PER_ACTION

    def floorchange(self, FloorLevelAnimeCount, FloorLevelAnimeSpeed):
        if FloorLevelAnimeCount > 0:
            self.y += FloorLevelAnimeSpeed
        else:
            self.y -= FloorLevelAnimeSpeed
    def collision(self,a): # 플레이어 정점과 충돌
        la, ta, ra, ba = self.get_bb()
        lb, tb, rb, bb = a.get_bb()
        print('start')
        if la > rb: return False
        print('1')
        if ra < lb: return False
        print('2')
        if ta < bb: return False
        print('3')
        if ba > tb: return False
        print('true')
        return True
    def get_bb(self):
        return self.x - 30 , self.y + 30 , self.x + 30 ,self.y - 30
ACTION_PER_TIME = 1.0 / 0.7
FRAMES_PER_ACTION = 8