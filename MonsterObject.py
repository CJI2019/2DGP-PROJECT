from pico2d import *
delayframe = 2
class MONSTER:
    def __init__(self):
        self.left_move_image = load_image('Monster/ghost_left.png')
        self.right_move_image = load_image('Monster/ghost_right.png')
        self.x , self.y= 300 , 300
        self.x1 , self.y1= self.x - (self.left_move_image.w//14) , self.y + (self.left_move_image.h//2)
        self.x2 , self.y2= self.x + (self.left_move_image.w//14) , self.y - (self.left_move_image.h//2)
        self.frame = 0
    def Draw(self):
        global delayframe
        # self.left_move_image.clip_draw(self.frame*(self.left_move_image.w//14),0,self.left_move_image.w//14,self.left_move_image.h,self.x,self.y)
        if self.frame < delayframe * 1:
            self.right_move_image.clip_draw(0*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 2:
            self.right_move_image.clip_draw(1*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 3:
            self.right_move_image.clip_draw(2*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 4:
            self.right_move_image.clip_draw(3*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 5:
            self.right_move_image.clip_draw(4*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 6:
            self.right_move_image.clip_draw(5*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 7:
            self.right_move_image.clip_draw(6*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 8:
            self.right_move_image.clip_draw(7*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 9:
            self.right_move_image.clip_draw(8*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 10:
            self.right_move_image.clip_draw(9*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 11:
            self.right_move_image.clip_draw(10*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 12:
            self.right_move_image.clip_draw(11*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
        elif self.frame < delayframe * 13:
            self.right_move_image.clip_draw(12*(self.right_move_image.w//14),0,self.right_move_image.w//14,self.right_move_image.h,self.x,self.y)
            self.frame = 2
        self.frame += 1
