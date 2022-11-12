import game_framework
import pico2d
import Main
import Game_title

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600

pico2d.open_canvas(GameWindow_WITDH,GameWindow_HEIGHT)
# game_framework.run(Main)
game_framework.run(Game_title)
pico2d.close_canvas()