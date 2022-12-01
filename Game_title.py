import game_framework
from pico2d import *

import Main

back = None
title_background = None
buttons = []
count = 0

game_difficulty = 'Easy'

class Button:
    NORMAL ,HARD = 0,0 # 각 난이도 1이면 열림 esay is default
    def __init__(self,x,y,raw,col):
        global count
        self.x ,self.y = x,y
        self.x1,self.y1 = self.x - raw, self.y + col
        self.x2,self.y2 = self.x + raw, self.y - col

        self.status = False
        if count == 0:
            self.image = load_image('Title/game_start.png')
        elif count == 1:
            self.image = load_image('Title/game_exit.png')
        elif count == 2:
            self.image = load_image('Title/game_easy.png')
        elif count == 3:
            self.image = load_image('Title/game_normal.png')
        elif count == 4:
            self.image = load_image('Title/game_hard.png')
        elif count == 5:
            self.image = load_image('Title/game_normal_lock.png')
        elif count == 6:
            self.image = load_image('Title/game_hard_lock.png')
        count += 1



    def draw(self):
        self.image.clip_composite_draw(0,0,self.image.w,self.image.h,0,'',self.x,self.y,self.x2 - self.x1 , self.y1 - self.y2)

    def collision(self,x, y):
        la, ta, ra, ba = self.get_bb()

        if la > x: return False
        if ra < x: return False
        if ta < y: return False
        if ba > y: return False

        return True
    def get_bb(self):
        return self.x1,self.y1,self.x2,self.y2

def enter():
    global back , buttons , count ,title_background
    if title_background == None:
        title_background = load_image('Title/title_background.png')
    back = load_image('Title/title.png')
    buttons += [Button(300,300,100,40)]
    buttons[0].status = True # start 버튼
    buttons += [Button(300,150,100,40)]
    buttons[1].status = True # quit 버튼
    buttons += [Button(300,300,100,40)] # esay
    buttons += [Button(300,200,100,40)] # normal
    buttons += [Button(300,100,100,40)] # hard
    if( Button.NORMAL == 0):
        buttons += [Button(300, 200, 100, 40)]  # normal lock
    else: count += 1

    if (Button.HARD == 0):
        buttons += [Button(300, 100, 100, 40)]  # hard lock

def exit():
    global buttons,count
    buttons.clear()
    count = 0
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    global game_difficulty
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type) == (SDL_MOUSEBUTTONDOWN):
            for idx , button in enumerate(buttons):
                if(button.status == False): continue
                if button.collision(event.x,600-event.y) == True:
                    # print('click')
                    if idx == 0 :
                        button.status = False
                        buttons[1].status = False
                        for i,b in enumerate(buttons):
                            if i > 1: b.status = True
                        break
                    elif idx == 1: # 종료 버튼
                        game_framework.quit()
                    elif idx == 2: # esay
                        game_difficulty = 'Easy'
                        game_framework.change_state(Main)
                    elif idx == 3 and Button.NORMAL == 1:  # Normal
                        game_difficulty = 'Normal'
                        game_framework.change_state(Main)
                    elif idx == 4 and Button.HARD == 1: # Hard
                        game_difficulty = 'Hard'
                        game_framework.change_state(Main)

def update():
    pass

def draw():
    global back , button , title_background
    clear_canvas()
    title_background.draw(300,300)
    # back.draw(300,300)
    for button in buttons:
        if button.status == True:
            button.draw()
    update_canvas()
