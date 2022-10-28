from pico2d import *

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600
#open canvas를 먼저 해야 load image 가능
open_canvas(GameWindow_WITDH,GameWindow_HEIGHT)

# Player 정보가 담겨있다
import PlayerObject
import FloorObject
import WaterObject
import WallObject

import MonsterObject
BackGround = load_image("back_2_2000.png")
BackGroundHeight = 0

""""""""""""""""""""""""
# 객체 생성
Water = WaterObject.WATER()
floors = [FloorObject.FLOOR() for i in range(FloorObject.SizeOfFloor())]
walls = [WallObject.WALL() for i in range(WallObject.SizeOfWall())]
Player = PlayerObject.PLAYER()
# 플레이어 y 값 초기화 발판으로 맞춤
Player.y = (floors[0].y1) + (Player.Right_Idle.h//2)
monsters = [MonsterObject.MONSTER()]
""""""""""""""""""""""""

while PlayerObject.play:
    clear_canvas()
    BackGround.clip_draw(0,(int)(BackGroundHeight),GameWindow_WITDH,GameWindow_HEIGHT
                    ,GameWindow_WITDH//2,GameWindow_HEIGHT//2)
    # 0.1 씩 배경 이미지 내려가게함.
    BackGroundHeight += 0.1
    if BackGround.h - (int)(BackGroundHeight) <= GameWindow_HEIGHT:
        BackGroundHeight = 0
    for floor in floors:
        floor.Draw()
    for wall in walls:
        wall.Draw()
    for monster in monsters:
        monster.Draw()
        monster.update(floors)

    Player.Player_Movement(floors,walls)
    PlayerObject.KeyDown_event(floors,Player,walls)
    FloorObject.FloorChange(Player,floors,Water,walls)
    FloorObject.FloorChange(Player,floors,Water,walls,monsters)
    
    Water.drawAupdate()
    Water.Crash(Player)
    update_canvas()

close_canvas()
