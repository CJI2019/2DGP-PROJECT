from pico2d import *
import time
GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600
#open canvas를 먼저 해야 load image 가능
open_canvas(GameWindow_WITDH,GameWindow_HEIGHT)

# Player 정보가 담겨있다
import PlayerObject
import FloorObject
import WaterObject
import WallObject
import MonsterObject
import skill
BackGround = load_image("back_2_2000.png")
BackGroundHeight = 0

""""""""""""""""""""""""
# 객체 생성
Water = WaterObject.WATER()
floors = [FloorObject.FLOOR() for i in range(FloorObject.SizeOfFloor())]
walls = [WallObject.WALL() for i in range(WallObject.SizeOfWall())]
Player = PlayerObject.PLAYER()
Skill = skill.SKILL()
# 플레이어 y 값 초기화 발판으로 맞춤
Player.y = (floors[0].y1) + (Player.Right_Idle.h//2)
if len(floors) > 3:
    monsters = [MonsterObject.MONSTER(3)]
else:
    monsters = []
""""""""""""""""""""""""
# 타이머 생성
timer = 0

frame_time = 0
current_time = time.time()
while PlayerObject.play:
    timer += 1
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
        if Skill.nodamegetime == 0:
            Player.MonsterCrash(monster)

    if len(floors) > Player.level + 3 and timer % 1000 == 0:
        monsters += [MonsterObject.MONSTER(floors[Player.level+3].level)]

    Player.Player_Movement(floors,walls,frame_time)
    PlayerObject.KeyDown_event(floors,Player,walls,Skill)

    FloorObject.FloorChange(Player,floors,Water,walls,monsters)
    
    Water.draw()

    # update
    Skill.update()
    # timestop 스킬을 사용했으면 update 밑 객체들은 업데이트 안함
    if Skill.skill_state[0] == None:
        # print(Skill.skill_state[0])
        if Skill.nodamegetime == 0 :
            Water.Crash(Player)
        # Water.update()
        for monster in monsters:
            monster.update(floors)

    update_canvas()
    frame_time = time.time() - current_time
    frame_rate = 1 / frame_time
    current_time += frame_time
    # print(f'Frame Time: {frame_time},  Frame Rate: {frame_rate}')

close_canvas()
