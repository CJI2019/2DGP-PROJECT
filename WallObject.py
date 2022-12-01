from pico2d import *
import Game_title
import PlayerObject

x = []
y = []

easyX = [500,124]
easyY = [2354,625]
normalX = [143,487,445,132]
normalY = [792,1130,1410,1728]
hardX = [138,565,134,106,256,380,145,71]
hardY = [1226, 1550, 1917, 2628, 4197, 4186, 4533, 4650]

xcount,ycount = 0,0 

class WALL:
    # def __init__(self,x,y): # maptool
    def __init__(self): # play
        # global x,y
        global xcount,ycount
        if Game_title.game_difficulty == 'Easy':
            self.image = load_image("Floor/wall_easy.png")
        elif Game_title.game_difficulty == 'Normal':
            self.image = load_image("Floor/wall_normal.png")
        elif Game_title.game_difficulty == 'Hard':
            self.image = load_image("Floor/wall_hard.png")
        # print("생성")
        self.x = x[xcount]; xcount += 1 #play
        self.y = y[ycount]; ycount += 1 #play
        # self.x = x; self.y = y # maptool
        self.x1 , self.y1= self.x - (self.image.w//2) , self.y + (self.image.h//2)
        self.x2 , self.y2= self.x + (self.image.w//2) , self.y - (self.image.h//2)
        # 화면에 그려질지 말지 플레이어와 부딫히면 그려짐.
        self.status = False # play
        # self.status = True # maptool

    def draw(self):
        if self.status:
            self.image.draw(self.x,self.y)
    def update(self):
        pass
    def Crash(self,player,index,frame_time):
        # 플레이어가 벽의 사각형 내에 있을때 (총 4개의 점)
        if (player.x1 > self.x1 and player.x1 < self.x2 and # 좌
        (player.y1+player.y2)//2 < self.y1 and (player.y1+player.y2)//2 > self.y2):
            if PlayerObject.xPos < 0 :
                player.WallCrash(frame_time); self.status = True
                # print("충돌")
            elif PlayerObject.xPos == 0 :
                player.x += 1; player.x1 += 1 ; player.x2 += 1
                # print("충돌")
        elif (player.x2 > self.x1 and player.x2 < self.x2 and # 우
        (player.y1+player.y2)//2 < self.y1 and (player.y1+player.y2)//2 > self.y2):
            if PlayerObject.xPos > 0 :
                player.WallCrash(frame_time); self.status = True
                # print("충돌")
            elif PlayerObject.xPos == 0 :
                player.x -= 1; player.x1 -= 1 ; player.x2 -= 1
                # print("충돌")
        elif ((player.x2+player.x1)//2 > self.x1 and (player.x2+player.x1)//2 < self.x2 and # 중앙
        (player.y1+player.y2)//2 < self.y1 and (player.y1+player.y2)//2 > self.y2):
            if (self.x1 + self.x2)//2 > (player.x2+player.x1)//2:
                player.x -= 5; player.x1 -= 5 ; player.x2 -= 5
            elif (self.x1 + self.x2)//2 < (player.x2+player.x1)//2:
                player.x += 5; player.x1 += 5 ; player.x2 += 5
            # print("중앙")
        elif ((player.x1+player.x2)//2 > self.x1 and (player.x1+player.x2)//2 < self.x2 and # 상
        player.y1 < self.y1 and player.y1 > self.y2):
            if PlayerObject.yPos != 0:
                player.y -= PlayerObject.yPos ; player.y1 -= PlayerObject.yPos ;player.y2 -= PlayerObject.yPos
            # print("충돌")
            self.status = True
        elif ((player.x1+player.x2)//2 > self.x1 and (player.x1+player.x2)//2 < self.x2 and # 하
        player.y2 < self.y1 and player.y2 > self.y2 and PlayerObject.FALLING):
            PlayerObject.JUMPKEYDOWN = False
            PlayerObject.FALLING = False; PlayerObject.yPos = 0
            player.y2 = self.y1; player.y = player.y2 + player.Right_Idle.h//2
            player.y1 = player.y + player.Right_Idle.h//2
            player.Wallpoint = index
            # print("충돌")
            self.status = True


def SizeOfWall():
    return len(x)