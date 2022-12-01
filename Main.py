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
BackGoundMusic = None

""""""""""""""""""""""""
Water = None
floors = None
walls = None
Player = None
Skill = None
Potal = None
monsters = None

#BackGround screen coodinate set
BackGround_window_left = 0
BackGround_window_bottom = 0
finish_floor_y = 0
# 타이머 생성
monsterSpawntime = 10
timer = monsterSpawntime
def enter():
    global BackGround,BackGroundHeight,timer,BackGoundMusic
    global Player , Skill , Potal , Water
    global floors,walls,monsters
    global monsterSpawntime
    timer = monsterSpawntime
    BackGroundHeight = 0

    # 객체 생성
    Water = WaterObject.WATER()
    game_world.add_object(Water,5)

    if Game_title.game_difficulty == 'Easy': # Easy 난이도
        BackGround = load_image("Title/back_easy.png")
        Water.speed = 0.3
        monsterSpawntime = 8
        FloorObject.x ,FloorObject.y = FloorObject.easyX , FloorObject.easyY
        FloorObject.floortype[:] = FloorObject.esayFloor
        WallObject.x,WallObject.y = WallObject.easyX,WallObject.easyY
        BackGoundMusic = load_music('Sound/sound_easy.mp3')
        BackGoundMusic.set_volume(30)
        BackGoundMusic.repeat_play()
    elif Game_title.game_difficulty == 'Normal': # Normal 난이도
        BackGround = load_image("Title/back_normal.png")
        Water.speed = 0.35
        monsterSpawntime = 6
        FloorObject.x ,FloorObject.y = FloorObject.normalX,FloorObject.normalY
        FloorObject.floortype[:] = FloorObject.normalFloor
        WallObject.x,WallObject.y = WallObject.normalX,WallObject.normalY
        BackGoundMusic = load_music('Sound/sound_normal.mp3')
        BackGoundMusic.set_volume(30)
        BackGoundMusic.repeat_play()
    elif Game_title.game_difficulty == 'Hard':  # Hard 난이도
        BackGround = load_image("Title/back_hard2.png")
        Water.speed = 0.37
        monsterSpawntime = 3
        FloorObject.x ,FloorObject.y = FloorObject.hardX,FloorObject.hardY
        FloorObject.floortype[:] = FloorObject.hardFloor
        WallObject.x,WallObject.y = WallObject.hardX,WallObject.hardY
        BackGoundMusic = load_music('Sound/sound_hard.mp3')
        BackGoundMusic.set_volume(30)
        BackGoundMusic.repeat_play()


    floors = [FloorObject.FLOOR() for i in range(FloorObject.SizeOfFloor())]
    game_world.add_objects(floors,0)
    global finish_floor_y
    finish_floor_y = floors[-1].yPos

    walls = [WallObject.WALL() for i in range(WallObject.SizeOfWall())]
    # walls = []
    game_world.add_objects(walls,1)

    Potal = potal.POTAL(floors[-1].xPos,floors[-1].y1+35)
    # Potal = potal.POTAL(floors[-1].xPos,floors[0].y1+35) # 임시 포탈
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
    global BackGround_window_left, BackGround_window_bottom


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
    BackGround_window_bottom = FloorObject.background_moveup(BackGround,finish_floor_y)
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(Game_title)
        else:
            # maptool_event(event)
            Player.handle_event(event)
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    global Player, Skill, Potal, Water, BackGround
    global floors, walls, monsters
    global BackGround , BackGround_window_left, BackGround_window_bottom

    BackGround.clip_draw_to_origin(BackGround_window_left, BackGround_window_bottom,
                                   GameWindow_WITDH, GameWindow_HEIGHT,
                                   0, 0)

    # BackGround.clip_draw(0, (int)(BackGroundHeight), GameWindow_WITDH, GameWindow_HEIGHT
    #                      , GameWindow_WITDH // 2, GameWindow_HEIGHT // 2)

    for game_object in game_world.all_objects():
        game_object.draw()

def exit():
    init_game()
    game_world.clear()
def pause():
    pass
def resume():
    pass

def init_game():
    global BackGround, BackGroundHeight, timer
    global BackGoundMusic
    # BackGoundMusic.stop()
    del BackGoundMusic
    BackGround = None
    BackGroundHeight = 0
    timer = monsterSpawntime

    PlayerObject.JUMPKEYDOWN = False
    PlayerObject.MoveRight, PlayerObject.MoveLeft = False, False
    PlayerObject.FALLING = False
    PlayerObject.frame = 0
    PlayerObject.xPos, PlayerObject.yPos = 0, 0
    PlayerObject.dir = 0
    PlayerObject.Current_KeyDown_List = [0, 0]

    FloorObject.xcount = 0
    FloorObject.ycount = 0
    FloorObject.level = 0
    FloorObject.Player_Floor_Level = 0
    FloorObject.FloorLevelAnimeCount = 0
    FloorObject.floor_changed_value = 0.0

    WallObject.xcount, WallObject.ycount = 0, 0
def add_monster():
    global monsters
    monsters += [MonsterObject.MONSTER(floors[Player.level + 3].level)]
    game_world.add_object(monsters[-1],3)

floortype = 1 # map tool variable
tool_name = 'floor' # map tool type
def maptool_event(event):
    global floortype,tool_name ,Player ,floors,walls
    if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
        if tool_name == 'floor':
            floors += [FloorObject.FLOOR(event.x,600-event.y,floortype)] # maptool
            game_world.add_object(floors[-1], 1)
        elif tool_name == 'wall':
            walls += [WallObject.WALL(event.x,600-event.y)]
            game_world.add_object(walls[-1], 1)
    elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
        if tool_name == 'floor':
            if floors[-1].level != Player.level:
                game_world.remove_object(floors.pop(len(floors)-1))
                # floors.pop(len(floors)-1)
                FloorObject.level -= 1
        elif tool_name == 'wall':
            if(len(walls)> 0):
                game_world.remove_object(walls.pop(len(walls)-1))
                # walls.pop(len(walls)-1)
    elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
        tool_name = 'wall'
        print("wall tool")
    elif event.type == SDL_KEYDOWN and event.key == SDLK_F2:
        tool_name = 'floor'
        print("floor tool")
    elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
        floortype = 1
    elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
        floortype = 2
    elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
        floortype = 3
    elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
        floortype = 4
    elif event.type == SDL_KEYDOWN and event.key == SDLK_5:
        floortype = 5
    elif event.type == SDL_KEYDOWN and event.key == SDLK_KP_PLUS: # 현재 플로어 정보 출력
        print('\nFloor x 좌표 출력')
        for floor in floors:
            print(floor.xPos,end = ',')
        print('\ny 좌표 출력')
        for floor in floors:
            print(floor.yPos - FloorObject.floor_changed_value,end = ',')
        print('\n이미지 타입 출력')
        for floor in floors:
            print(floor.floortype,end = ',')
        print('\nWall x 좌표 출력')
        for wall in walls:
            print(wall.x,end = ',')
        print('\ny 좌표 출력')
        for wall in walls:
            print(wall.y - FloorObject.floor_changed_value,end = ',')
        print('\n') # map tool end

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KPH = 15  # km/h
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER
