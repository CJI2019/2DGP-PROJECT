from pico2d import *
import game_framework
import Game_title
import time

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600
#open canvas를 먼저 해야 load image 가

import PlayerObject
import FloorObject
import WaterObject
import WallObject
import MonsterObject
import skill
import Potal as potal

BackGround = None
BackGroundHeight = 0

""""""""""""""""""""""""
Water = None
floors = None
walls = None
Player = None
Skill = None
Potal = None
monsters = None
def enter():
    global Player , Skill , Potal , Water ,BackGround
    global floors,walls,monsters
    # 객체 생성
    BackGround = load_image("back_2_2000.png")

    Water = WaterObject.WATER()
    floors = [FloorObject.FLOOR() for i in range(FloorObject.SizeOfFloor())]
    walls = [WallObject.WALL() for i in range(WallObject.SizeOfWall())]
    Player = PlayerObject.PLAYER()
    Skill = skill.SKILL()
    # Potal = potal.POTAL(floors[-1].xPos,floors[-1].y1+35)
    Potal = potal.POTAL(floors[-1].xPos,floors[0].y1+35)

    # 플레이어 y 값 초기화 발판으로 맞춤
    Player.y = (floors[0].y1) + (Player.Right_Idle.h//2)
    Player.y1, Player.y2 = Player.y + (Player.Right_Idle.h // 2), Player.y - (Player.Right_Idle.h // 2)
    if len(floors) > 3:
        monsters = [MonsterObject.MONSTER(3)]
    else:
        monsters = []

""""""""""""""""""""""""
# 타이머 생성
timer = 0

frame_time = 0
current_time = time.time()
def update():
    global timer ,BackGroundHeight ,monsters ,frame_time ,current_time
    global Player, Skill, Potal, Water, BackGround
    timer += 1
    # clear_canvas()
    # BackGround.clip_draw(0,(int)(BackGroundHeight),GameWindow_WITDH,GameWindow_HEIGHT
    #                 ,GameWindow_WITDH//2,GameWindow_HEIGHT//2)
    # 0.1 씩 배경 이미지 내려가게함.
    BackGroundHeight += 0.1
    if BackGround.h - (int)(BackGroundHeight) <= GameWindow_HEIGHT:
        BackGroundHeight = 0
    # for floor in floors:
    #     floor.Draw()
    # for wall in walls:
    #     wall.Draw()
    for monster in monsters:
        # monster.Draw()
        if Skill.nodamegetime == 0:
            Player.MonsterCrash(monster)

    if len(floors) > Player.level + 3 and timer % 1000 == 0:
        monsters += [MonsterObject.MONSTER(floors[Player.level+3].level)]

    # Potal.draw()
    # draw_rectangle(*Potal.get_bb())  # 튜플을 넘길때 *을 붙히면 튜플을 펼쳐줌
    Potal.update(frame_time)
    Player.update(floors,walls,frame_time)
    # Player.Player_Movement(floors,walls,frame_time)
    # draw_rectangle(*Player.get_bb())  # 튜플을 넘길때 *을 붙히면 튜플을 펼쳐줌
    # PlayerObject.KeyDown_event(floors,Player,walls,Skill,monsters,Potal)

    FloorObject.FloorChange(Player,floors,Water,walls,monsters,Potal)
    
    # Water.draw()
    # Skill.draw(Player)
    # update
    Skill.update(frame_time)
    # timestop 스킬을 사용했으면 update 밑 객체들은 업데이트 안함
    if Skill.skill_state[0] == None:
        # print(Skill.skill_state[0])
        if Skill.nodamegetime == 0:
            Water.Crash(Player)
        Water.update()
        for monster in monsters:
            monster.update(floors,frame_time)

    # update_canvas()
    frame_time = time.time() - current_time
    frame_rate = 1 / frame_time
    current_time += frame_time
    # print(f'Frame Time: {frame_time},  Frame Rate: {frame_rate}')

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(Game_title)
        else:
            PlayerObject.KeyDown_event(event,floors,Player,walls,Skill,monsters,Potal)
def draw():

    clear_canvas()
    BackGround.clip_draw(0, (int)(BackGroundHeight), GameWindow_WITDH, GameWindow_HEIGHT
                         , GameWindow_WITDH // 2, GameWindow_HEIGHT // 2)

    for floor in floors:
        floor.Draw()
    for wall in walls:
        wall.Draw()

    for monster in monsters:
        monster.Draw()

    Potal.draw()
    draw_rectangle(*Potal.get_bb())  # 튜플을 넘길때 *을 붙히면 튜플을 펼쳐줌

    Player.draw(frame_time)
    draw_rectangle(*Player.get_bb())  # 튜플을 넘길때 *을 붙히면 튜플을 펼쳐줌

    # Water.draw()
    Skill.draw(Player)
    update_canvas()

def exit():
    pass
