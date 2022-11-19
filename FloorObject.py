from pico2d import *
import random

import game_framework

GameWindow_WITDH , GameWindow_HEIGHT = 600,600

# 맵툴로 스테이지 별로 만들어 두고 이 곳에 삽입하면 됨.
easyX = [] # maptool
easyY = []
nomalX = []
nomalY = []
hardX = []
hardY = []

x = [GameWindow_WITDH//2,89,457,580,114,527,158,442,278,500,428,153,434] # maptool
y = [GameWindow_HEIGHT//20,191,296,413,535,655,777,897,1008,1121,1245,1355,1505] # maptool

floortype = [0,2,2,2,2,3,4,4,4,4,4,3,3]

xcount = 0
ycount = 0

# Floor index : 플레이어가 어디발판에 있는지 확인
level = 0
class FLOOR:
    # def __init__(self,x=None,y=None,floortype = None): # maptool
    def __init__(self): # play
    #     global x,y , floortype
        global xcount,ycount,level
        # if x == None: x = GameWindow_WITDH//2 # maptool
        # if y == None: y = GameWindow_HEIGHT//20 # maptool
        # if floortype == None:
        #     floortype = random.randint(0,5) +1 
        self.floortype = floortype[xcount] # play
        # self.floortype = floortype # maptool
        self.image = None
        if(xcount == 0):
            self.image = load_image("Floor\main_floor_1.png")
        else:
            self.image = load_image("Floor/floor_0{0}.png".format(floortype[xcount])) # play
            # self.image = load_image("Floor/floor_0{0}.png".format(floortype)) # maptool
        self.level = level
        level += 1
        # floor 의 위치
        self.xPos = x[xcount] # play
        # self.xPos = x # map tool
        xcount += 1
        self.yPos = y[ycount] #play
        # self.yPos = y # map tool
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
# floor 에 따른 애니메이션 속도
# FloorLevelAnimeSpeed = 10

def FloorChange(Player,floors,Water,walls,monsters,potal):
    global Player_Floor_Level ,FloorLevelAnimeCount,FloorLevelAnimeSpeed

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
        