from pico2d import *

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600
#open canvas를 먼저 해야 load image 가능
open_canvas(GameWindow_WITDH,GameWindow_HEIGHT)

# Player 정보가 담겨있다
import PlayerObject
import FloorObject
import WaterObject
import WallObject

BackGround = load_image("back_2_2000.png")
BackGroundHeight = 0


# 객체 생성
Water = WaterObject.WATER()
floors = [FloorObject.FLOOR() for i in range(FloorObject.SizeOfFloor())]
walls = [WallObject.WALL() for i in range(WallObject.SizeOfWall())]
Player = PlayerObject.PLAYER() 
Player.y = (floors[0].y1) + (Player.Right_Idle.h//2) 
Player.x1, Player.y1 = Player.x - (Player.Right_Idle.w//8), Player.y + (Player.Right_Idle.h//2)
Player.x2, Player.y2 = Player.x + (Player.Right_Idle.w//8), Player.y - (Player.Right_Idle.h//2)

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
    Player.Player_Movement(floors,walls)
    PlayerObject.KeyDown_event(floors,Player,walls)
    FloorObject.FloorChange(Player,floors,Water,walls)
    
    Water.drawAupdate()
    Water.Crash(Player)
    update_canvas()

close_canvas()
