from pico2d import *


class MONSTER:
    # animation delaytime
    delayframe = 2
    def __init__(self):
        self.left_move_image = load_image('Monster/ghost_left.png')
        self.right_move_image = load_image('Monster/ghost_right.png')
        self.x , self.y= 300 , 300
        self.x1 , self.y1= self.x - (self.left_move_image.w//14) , self.y + (self.left_move_image.h//2)
        self.x2 , self.y2= self.x + (self.left_move_image.w//14) , self.y - (self.left_move_image.h//2)
        self.frame = 0
    def Draw(self):
        for i in range(0,13):
            if self.frame < MONSTER.delayframe * (i+1):
                self.right_move_image.clip_draw(i * (self.right_move_image.w // 14), 0, self.right_move_image.w // 14, self.right_move_image.h, self.x, self.y)
                if i == 13 - 1:
                    self.frame = 2
                break
        self.frame += 1
