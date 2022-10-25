from pico2d import *
import PlayerObject
# x = []
# y = []

x = [433,114] # maptool
y = [777,1355]
xcount,ycount = 0,0 

class WALL:
    # def __init__(self,x,y): # maptool
    def __init__(self):
        # global x,y
        global xcount,ycount
        self.image = load_image('wall.png')
        print("생성")
        self.x = x[xcount]; xcount += 1
        self.y = y[ycount]; ycount += 1
        # self.x = x; self.y = y
        self.x1 , self.y1= self.x - (self.image.w//2) , self.y + (self.image.h//2)
        self.x2 , self.y2= self.x + (self.image.w//2) , self.y - (self.image.h//2)
        # 화면에 그려질지 말지 플레이어와 부딫히면 그려짐.
        self.status = False
    def Draw(self):
        if not self.status:
            self.image.draw(self.x,self.y)
    def Crash(self,player,index):
        # 플레이어가 벽의 사각형 내에 있을때 (총 4개의 점)
        if (player.x1 > self.x1 and player.x1 < self.x2 and # 좌
        (player.y1+player.y2)//2 < self.y1 and (player.y1+player.y2)//2 > self.y2 and
        PlayerObject.xPos < 0):
            player.WallCrash()
            print("충돌")
            elif PlayerObject.xPos == 0 :
                player.x += 1; player.x1 += 1 ; player.x2 += 1
                print("충돌")
        elif (player.x2 > self.x1 and player.x2 < self.x2 and # 우
        (player.y1+player.y2)//2 < self.y1 and (player.y1+player.y2)//2 > self.y2 and
        PlayerObject.xPos > 0):
            player.WallCrash()
            print("충돌")
            elif PlayerObject.xPos == 0 :
                player.x -= 1; player.x1 -= 1 ; player.x2 -= 1
                print("충돌")
        elif ((player.x2+player.x1)//2 > self.x1 and (player.x2+player.x1)//2 < self.x2 and # 중앙
        (player.y1+player.y2)//2 < self.y1 and (player.y1+player.y2)//2 > self.y2):
            if (self.x1 + self.x2)//2 > (player.x2+player.x1)//2:
                player.x -= 5; player.x1 -= 5 ; player.x2 -= 5
            elif (self.x1 + self.x2)//2 < (player.x2+player.x1)//2:
                player.x += 5; player.x1 += 5 ; player.x2 += 5
        elif ((player.x1+player.x2)//2 > self.x1 and (player.x1+player.x2)//2 < self.x2 and # 상
        player.y1 < self.y1 and player.y1 > self.y2 ):
            if PlayerObject.yPos != 0:
                player.y -= PlayerObject.yPos ; player.y1 -= PlayerObject.yPos ;player.y2 -= PlayerObject.yPos
            print("충돌")
        elif ((player.x1+player.x2)//2 > self.x1 and (player.x1+player.x2)//2 < self.x2 and # 하
        player.y2 < self.y1 and player.y2 > self.y2 and PlayerObject.FALLING):
            PlayerObject.JUMPKEYDOWN = False
            PlayerObject.FALLING = False; PlayerObject.yPos = 0
            player.y2 = self.y1; player.y = player.y2 + player.Right_Idle.h//2
            player.y1 = player.y + player.Right_Idle.h//2
            player.Wallpoint = index
            print("충돌")


def SizeOfWall():
    return len(x)