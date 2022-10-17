from pico2d import *
import PlayerObject

class WALL:
    def __init__(self,x,y):
        self.image = load_image('wall.png')
        print("생성")
        self.x = x
        self.y = y
        self.x1 , self.y1= x - (self.image.w//2) , y + (self.image.h//2)
        self.x2 , self.y2= x + (self.image.w//2) , y - (self.image.h//2)
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
        elif (player.x2 > self.x1 and player.x2 < self.x2 and # 우
        (player.y1+player.y2)//2 < self.y1 and (player.y1+player.y2)//2 > self.y2 and
        PlayerObject.xPos > 0):
            player.WallCrash()
            print("충돌")
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
