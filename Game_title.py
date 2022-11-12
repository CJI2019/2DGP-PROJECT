import game_framework
from pico2d import *

import Main

back = None
buttons = []
count = 0
class Button:
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
    global back , buttons
    back = load_image('Title/title.png')
    buttons += [Button(300,300,100,40)]
    buttons[0].status = True # start 버튼
    buttons += [Button(300,150,100,40)]
    buttons[1].status = True # quit 버튼
    buttons += [Button(300,400,100,40)] # esay
    buttons += [Button(300,300,100,40)] # normal
    buttons += [Button(300,200,100,40)] # hard

def exit():
    global back , buttons
    del back , buttons

def pause():
    pass

def resume():
    pass

def handle_events():
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
                    print('click')
                    if idx == 0 :
                        button.status = False
                        buttons[1].status = False
                        for i,b in enumerate(buttons):
                            if i > 1: b.status = True
                    elif idx == 1: # 종료 버튼
                        game_framework.quit()
                    elif idx == 2: # esay
                        game_framework.change_state(Main)

def update():
    pass

def draw():
    global back , button
    clear_canvas()
    back.draw(300,300)
    for button in buttons:
        if button.status == True:
            button.draw()
    update_canvas()
    pass
