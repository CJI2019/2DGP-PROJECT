from pico2d import *

import Main
import game_framework
from Main import draw_world

gameover = None
game_restart = None
game_title = None
def enter():
    global game_title,game_restart,gameover

    if gameover == None:
        gameover = load_image('Title/game_over.png')
        game_restart = load_image('Title/game_restart.png')
        game_title = load_image('Title/game_title.png')

def draw():
    clear_canvas()
    draw_world()

    gameover.draw(300, 400)
    game_restart.clip_composite_draw(0, 0, game_restart.w, game_restart.h, 0, '', 200, 250, 100, 50)
    game_title.clip_composite_draw(0, 0, game_title.w, game_title.h, 0, '', 400, 250, 100, 50)

    update_canvas()
def update():
    pass

def restart_click(x,y):
    y = 600 - y
    if x > 250: return
    if x < 150: return
    if y > 300: return
    if y < 200: return

    Main.exit()
    Main.enter()
    game_framework.pop_state()

def title_click(x,y):
    y = 600 - y

    if x > 450: return
    if x < 350: return
    if y > 300: return
    if y < 200: return

    import Game_title
    game_framework.pop_state()
    game_framework.change_state(Game_title)

def handle_events():
    events = get_events()

    for event in events:
        if (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE) or (event.type == SDL_QUIT):
            game_framework.quit()
        if event.type == SDL_MOUSEBUTTONDOWN:
            restart_click(event.x,event.y)
            title_click(event.x,event.y)


def exit():

    pass
def pause():
    pass
def resume():
    pass

