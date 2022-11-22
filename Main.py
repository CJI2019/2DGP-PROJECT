from pico2d import *
import game_framework
import Game_title
import game_world

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600

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

# 타이머 생성
monsterSpawntime = 10
timer = monsterSpawntime
def enter():
    global BackGround,BackGroundHeight,timer
    global Player , Skill , Potal , Water
    global floors,walls,monsters
    global monsterSpawntime

    timer = monsterSpawntime
    BackGroundHeight = 0

    # 객체 생성
    BackGround = load_image("back_2_2000.png")
    # game_world.add_object(BackGround,0)

    Water = WaterObject.WATER()
    game_world.add_object(Water,5)

    if Game_title.game_difficulty == 'Easy': # Easy 난이도
        Water.speed = 0.25
        monsterSpawntime = 10
        # FloorObject.x ,FloorObject.y = FloorObject.easyX , FloorObject.easyY
        # FloorObject.floortype[:] = FloorObject.esayFloor
        WallObject.x,WallObject.y = WallObject.easyX,WallObject.easyY
    elif Game_title.game_difficulty == 'Normal': # Normal 난이도
        Water.speed = 0.5
        monsterSpawntime = 8
        FloorObject.x ,FloorObject.y = FloorObject.normalX,FloorObject.normalY
        WallObject.x,WallObject.y = WallObject.normalX,WallObject.normalY

    elif Game_title.game_difficulty == 'Hard':  # Hard 난이도
        Water.speed = 1.0
        monsterSpawntime = 6
        FloorObject.x ,FloorObject.y = FloorObject.hardX,FloorObject.hardY
        WallObject.x,WallObject.y = WallObject.hardX,WallObject.hardY


    floors = [FloorObject.FLOOR() for i in range(FloorObject.SizeOfFloor())]
    game_world.add_objects(floors,0)

    # walls = [WallObject.WALL() for i in range(WallObject.SizeOfWall())]
    walls = []
    game_world.add_objects(walls,1)

    # Potal = potal.POTAL(floors[-1].xPos,floors[-1].y1+35)
    Potal = potal.POTAL(floors[-1].xPos,floors[0].y1+35) # 임시 포탈
    game_world.add_object(Potal,2)


    if len(floors) > 3:
        monsters = [MonsterObject.MONSTER(3)]
    else:
        monsters = []
    game_world.add_objects(monsters,3)

    Player = PlayerObject.PLAYER()
    game_world.add_object(Player, 4)
    # 플레이어 y 값 초기화 발판으로 맞춤
    Player.y = (floors[0].y1) + (Player.Right_Idle.h // 2)
    Player.y1, Player.y2 = Player.y + (Player.Right_Idle.h // 2), Player.y - (Player.Right_Idle.h // 2)

    Skill = skill.SKILL()
    game_world.add_object(Skill, 6)


""""""""""""""""""""""""

def update():
    global BackGround , timer,BackGroundHeight


    # 0.1 씩 배경 이미지 내려가게함.
    BackGroundHeight += 0.05 * RUN_SPEED_PPS * game_framework.frame_time
    if BackGround.h - (int)(BackGroundHeight) <= GameWindow_HEIGHT:
        BackGroundHeight = 0
    timer -= game_framework.frame_time
    if len(floors) > Player.level + 3 and timer < 0:  # 일정 시간 마다 몬스터 생성
        timer = monsterSpawntime
        add_monster()

    for game_object in game_world.all_objects():
        game_object.update()

    FloorObject.FloorChange(Player,floors,Water,walls,monsters,Potal)

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




def exit():
    pass
