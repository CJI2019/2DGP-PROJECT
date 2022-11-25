from pico2d import *
import random

import game_framework
import Game_title

GameWindow_WITDH , GameWindow_HEIGHT = 600,600

# 맵툴로 스테이지 별로 만들어 두고 이 곳에 삽입하면 됨.
easyX = [GameWindow_WITDH//2,118,408,261,341,342,342,175,485,192,417,206,224,414,414,414,157,300,330,448,271,0,393,247]
easyY = [GameWindow_HEIGHT//20, 230, 338, 445, 561, 681, 793, 907, 1038, 1163, 1281, 1413, 1547, 1656, 1769, 1882, 2026, 2159, 2282, 2389, 2497, 2614, 2714, 2821]
esayFloor = [0,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,5,1,1]
normalX = [GameWindow_WITDH//2,137,405,219,368,309,309,309,309,189,356,28,581,185,267,86,351,198,393,513,260,113,364,525,328,7,398,156,465,175,483,119,455,220]
normalY = [GameWindow_HEIGHT//20, 234, 354, 462, 566, 684, 796, 908, 1020, 1141, 1271, 1392, 1440, 1567, 1711, 1842, 1968, 2097, 2223, 2343, 2462, 2587, 2704, 2815, 2925, 3051, 3114, 3239, 3353, 3483, 3582, 3657, 3717, 3853]
normalFloor = [0,1,1,1,1,5,5,5,5,3,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1]
hardX = [GameWindow_WITDH//2,206,395,249,393,215,415,232,441,346,345,345,345,345,345,345,224,224,224,318,318,318,291,483,218,438,139,468,147,180,260,131,475,133,366,387,387,387,194,299,291]
hardY = [GameWindow_HEIGHT//20,220, 333, 455, 568, 675, 786, 903, 1016, 1134, 1246, 1357, 1472, 1584, 1697, 1809, 1932, 2045, 2157, 2281, 2393, 2506, 2636, 2742, 2869, 2969, 3077, 3175, 3276, 3396, 3516, 3622, 3695, 3777, 3896, 4016, 4131, 4244, 4360, 4493, 4825]
hardFloor = [0,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,4,4]

x = [GameWindow_WITDH//2]
y = [GameWindow_HEIGHT//20]

floortype = [0]

xcount = 0
ycount = 0

# Floor index : 플레이어가 어디발판에 있는지 확인
level = 0
class FLOOR:
    # def __init__(self,xpos = None,ypos = None,floortype = None): # maptool
    def __init__(self): # play
    #     global x,y , floortype
        global xcount,ycount,level
        # if xpos == None: xpos = GameWindow_WITDH//2 # maptool
        # if ypos == None: ypos = GameWindow_HEIGHT//20 # maptool
        # self.floortype = floortype  # maptool

        self.floortype = floortype[xcount] # play
        self.image = None
        if(xcount == 0):
            if Game_title.game_difficulty == 'Easy':
                self.image = load_image("Floor/main_floor_easy_01.png")
            elif Game_title.game_difficulty == 'Normal':
                self.image = load_image("Floor/main_floor_normal_01.png")
            elif Game_title.game_difficulty == 'Hard':
                self.image = load_image("Floor/main_floor_hard_01.png")
        else:
            if Game_title.game_difficulty == 'Easy':
                self.image = load_image("Floor/floor_easy_0{0}.png".format(floortype[xcount]))  # play
            elif Game_title.game_difficulty == 'Normal':
                self.image = load_image("Floor/floor_normal_0{0}.png".format(floortype[xcount]))  # play
            elif Game_title.game_difficulty == 'Hard':
                self.image = load_image("Floor/floor_hard_0{0}.png".format(floortype[xcount]))  # play
            # self.image = load_image("Floor/floor_0{0}.png".format(floortype)) # maptool
        self.level = level
        level += 1
        # floor 의 위치
        self.xPos = x[xcount] # play
        # self.xPos = xpos # map tool
        xcount += 1
        self.yPos = y[ycount] #play
        # self.yPos = ypos # map tool
        ycount += 1
        # floor 의 영역
        self.x1 ,self.y1 = self.xPos - self.image.w//2 + 10, self.yPos + self.image.h//2
        self.x2 ,self.y2 = self.xPos + self.image.w//2 - 10, self.yPos
    def draw(self):
        self.image.draw(self.xPos,self.yPos)
    def update(self):
        pass


def SizeOfFloor():
    return len(x)


PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KPH = 120 # km/h
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

# 플레이어 현재 floor 레벨
Player_Floor_Level = 0
# floor 레벨 변화
FloorLevelAnimeCount = 0
floor_changed_value = 0.0
# floor 변화에 따른 애니메이션 속도
FloorLevelAnimeSpeed = 0.0
def FloorChange(Player,floors,Water,walls,monsters,potal):
    global Player_Floor_Level ,FloorLevelAnimeCount,FloorLevelAnimeSpeed
    global floor_changed_value

    FloorLevelAnimeSpeed = RUN_SPEED_PPS * game_framework.frame_time

    if (Player_Floor_Level != Player.CompliteLevel and FloorLevelAnimeCount == 0):
        FloorLevelAnimeCount = (Player_Floor_Level - Player.CompliteLevel) * 0.1 # 높아 지면 음수
        Player_Floor_Level = Player.CompliteLevel
        
    if(FloorLevelAnimeCount != 0):
        # 한 단계당 FloorLevelAnimeSpeed 에 따라 위치 변함.
        for floor in floors:
            if FloorLevelAnimeCount > 0:
                floor.y1 += FloorLevelAnimeSpeed; floor.y2 += FloorLevelAnimeSpeed
                floor.yPos += FloorLevelAnimeSpeed
            else :
                floor.y1 -= FloorLevelAnimeSpeed; floor.y2 -= FloorLevelAnimeSpeed
                floor.yPos -= FloorLevelAnimeSpeed
        if FloorLevelAnimeCount > 0:
            floor_changed_value += FloorLevelAnimeSpeed
        else:
            floor_changed_value -= FloorLevelAnimeSpeed
        for wall in walls:
            if FloorLevelAnimeCount > 0:
                wall.y += FloorLevelAnimeSpeed
                wall.y1 += FloorLevelAnimeSpeed
                wall.y2 += FloorLevelAnimeSpeed
            else :
                wall.y -= FloorLevelAnimeSpeed
                wall.y1 -= FloorLevelAnimeSpeed
                wall.y2 -= FloorLevelAnimeSpeed
        for monster in monsters:
            monster.floorchange(FloorLevelAnimeCount,FloorLevelAnimeSpeed)
        potal.floorchange(FloorLevelAnimeCount,FloorLevelAnimeSpeed)
        if FloorLevelAnimeCount > 0:
            Water.y += FloorLevelAnimeSpeed
        else :
            Water.y -= FloorLevelAnimeSpeed
        # 플레이어 좌표 y값 floor 에 맞추기
        Player.CoordinateInput(floors[Player.CompliteLevel].y1 + Player.Right_Idle.h//2)
        if FloorLevelAnimeCount > 0 :
            FloorLevelAnimeCount -= game_framework.frame_time
            if FloorLevelAnimeCount < 0:
                FloorLevelAnimeCount = 0
        else:
            FloorLevelAnimeCount += game_framework.frame_time
            if FloorLevelAnimeCount > 0:
                FloorLevelAnimeCount = 0

def background_moveup(BackGround,finish_y):
    return clamp(0, (int)(-floor_changed_value/int(finish_y/GameWindow_HEIGHT)), BackGround.h - GameWindow_HEIGHT - 1)
