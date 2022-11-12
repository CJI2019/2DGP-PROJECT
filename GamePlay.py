import game_framework
import pico2d
import Main

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600

pico2d.open_canvas(GameWindow_WITDH,GameWindow_HEIGHT)
game_framework.run(Main)
pico2d.close_canvas()