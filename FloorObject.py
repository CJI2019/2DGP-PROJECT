from pico2d import *
import random
# import WaterObject
GameWindow_WITDH , GameWindow_HEIGHT = 600,600

# x = [GameWindow_WITDH//2] # maptool
# y = [GameWindow_HEIGHT//20] # maptool
# floor 를 저장 할 값
x = [GameWindow_WITDH//2,136,420,225,343,359,360,238,372,415,154,333]
y = [GameWindow_HEIGHT//20,198,307,407,516,649,749,959,1064,1180,1312,1433]
floortype = [1,1,1,1,3,3,3,4,3,3,3,4,]
# while True:       # map tool 용 완성시 주석 해제
#     r = random.randint(0,1)
#     if r == 0: 
#         x += [random.randint(1,4) * 100]
#         y += [100 * len(x)]
#     elif r == 1:
#         x += [random.randint(2,6) * 100]
#         y += [100 * len(x)]
#     if len(x) == 100: break

xcount = 0
ycount = 0
# Floor index : 플레이어가 어디발판에 있는지 확인
level = 0
class FLOOR:
    # def __init__(self,x=None,y=None,floortype = None): # maptool
    def __init__(self):
        global x,y , floortype
        global xcount,ycount,level
        # if x == None: x = GameWindow_WITDH//2 # maptool
        # if y == None: y = GameWindow_HEIGHT//20
        # if floortype == None:
        #     floortype = random.randint(0,5) +1 
        self.floortype = floortype[xcount]
        # self.floortype = floortype # maptool
        if(xcount == 0):
            self.image = load_image("Floor\main_floor_1.png")
        else:
            self.image = load_image("Floor/floor_0{0}.png".format(floortype[xcount]))
            # self.image = load_image("Floor/floor_0{0}.png".format(floortype)) # maptool
        self.level = level
        level += 1
        # floor 의 위치
        self.xPos = x[xcount]
        # self.xPos = x # map tool
        xcount += 1
        self.yPos = y[ycount]
        # self.yPos = y # map tool
        ycount += 1
        # floor 의 영역
        self.x1 ,self.y1 = self.xPos - self.image.w//2 + 10, self.yPos + self.image.h//2
        self.x2 ,self.y2 = self.xPos + self.image.w//2 - 10, self.yPos
        # self.x2 ,self.y2 = self.xPos + self.image.w//2 - 10, self.yPos - self.image.h//2
    def Draw(self):
        self.image.draw(self.xPos,self.yPos)


def SizeOfFloor():
    return len(x)

# 플레이어 현재 floor 레벨
Player_Floor_Level = 0
# floor 레벨 변화
FloorLevelAnimeCount = 0
# floor 에 따른 애니메이션 속도
FloorLevelAnimeSpeed = 10 

def FloorChange(Player,floors,Water,walls,monsters):
    global Player_Floor_Level ,FloorLevelAnimeCount,FloorLevelAnimeSpeed

    if (Player_Floor_Level != Player.CompliteLevel and FloorLevelAnimeCount == 0):
        FloorLevelAnimeCount = (Player_Floor_Level - Player.CompliteLevel) * FloorLevelAnimeSpeed # 높아 지면 음수 
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
        if FloorLevelAnimeCount > 0:
            Water.y += FloorLevelAnimeSpeed
        else :
            Water.y -= FloorLevelAnimeSpeed
        # 플레이어 좌표 y값 floor 에 맞추기
        Player.CoordinateInput(floors[Player.CompliteLevel].y1 + Player.Right_Idle.h//2)
        if FloorLevelAnimeCount > 0 :
            FloorLevelAnimeCount -= 1
        else:
            FloorLevelAnimeCount += 1
        