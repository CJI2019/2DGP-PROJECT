import random

from pico2d import *


class MONSTER:
    # animation delaytime
    delayframe = 2
    def __init__(self,floorlevel):
        self.left_move_image = load_image('Monster/ghost_left.png')
        self.right_move_image = load_image('Monster/ghost_right.png')
        self.x , self.y= random.randint(0,600) , 600
        self.x1 , self.y1= self.x - (self.left_move_image.w//14) , self.y + (self.left_move_image.h//2)
        self.x2 , self.y2= self.x + (self.left_move_image.w//14) , self.y - (self.left_move_image.h//2)
        self.frame = 0
        self.dir = 0
        self.floorlevel = floorlevel
    def Draw(self):
        for i in range(0,13):
            if self.frame < MONSTER.delayframe * (i+1):
                if self.dir == 0:
                    self.right_move_image.clip_draw(i * (self.right_move_image.w // 14), 0, self.right_move_image.w // 14, self.right_move_image.h, self.x, self.y)
                elif self.dir == 1:
                    self.left_move_image.clip_draw(i * (self.left_move_image.w // 14), 0, self.left_move_image.w // 14, self.left_move_image.h, self.x, self.y)
                if i == 13 - 1:
                    self.frame = 2
                break
        self.frame += 1
    def update(self,floors):
        if self.dir == 0:
            self.x += 0.5; self.x1 += 0.5; self.x2 += 0.5
            if self.x > 600:
                self.dir = 1
        elif self.dir == 1:
            self.x -= 0.5; self.x1 -= 0.5; self.x2 -= 0.5
            if self.x < 0:
                self.dir = 0
        self.y -= 1; self.y1 -= 1; self.y2 -= 1
        # for floor in floors:
        #     if floor.x1 < self.x and self.x < floor.x2 and floor.y2 < self.y2 and self.y2 < floor.y1:
        #         self.y = (floor.y1 + self.right_move_image.h//2)
        #         self.y1 = self.y + self.right_move_image.h//2
        #         self.y2 = self.y - self.right_move_image.h//2
        #         break
        if floors[self.floorlevel].x1 < self.x and self.x < floors[self.floorlevel].x2 and floors[self.floorlevel].y2 < self.y2 and self.y2 < floors[self.floorlevel].y1:
            self.y = (floors[self.floorlevel].y1 + self.right_move_image.h//2)
            self.y1 = self.y + self.right_move_image.h//2
            self.y2 = self.y - self.right_move_image.h//2
        if floors[self.floorlevel].x1 > self.x or floors[self.floorlevel].x2 < self.x:
            self.floorlevel -= 1

    def floorchange(self, FloorLevelAnimeCount, FloorLevelAnimeSpeed):
        if FloorLevelAnimeCount > 0:
            self.y += FloorLevelAnimeSpeed
            self.y1 += FloorLevelAnimeSpeed
            self.y2 += FloorLevelAnimeSpeed
        else:
            self.y -= FloorLevelAnimeSpeed
            self.y1 -= FloorLevelAnimeSpeed
            self.y2 -= FloorLevelAnimeSpeed