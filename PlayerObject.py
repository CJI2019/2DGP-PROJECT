from pico2d import *
import WallObject
GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600
# 점프 높이
JUMPHEIGHT = 14

JUMPKEYDOWN = False
class PLAYER:
    def __init__(self):
        self.Left_Idle = load_image('Player\Player_left_idle.png')
        self.Right_Idle = load_image('Player\Player_right_idle.png')

        self.Left_Run = load_image('Player\Player_left_run.png')
        self.Right_Run = load_image('Player\Player_right_run.png')

        self.Left_Jump = load_image('Player\Player_left_jump.png')
        self.Right_Jump = load_image('Player\Player_right_jump.png')
        self.Left_Fall = load_image('Player\Player_left_fall.png')
        self.Right_Fall = load_image('Player\Player_right_fall.png')
        self.x = 300
        self.y = 300
        # 좌 상
        self.x1, self.y1 = self.x - (self.Right_Idle.w//8), self.y + (self.Right_Idle.h//2)
        # 우 하
        self.x2, self.y2 = self.x + (self.Right_Idle.w//8), self.y - (self.Right_Idle.h//2)
        self.Wallpoint = -1
        # 현재 floor 판별
        self.level = 0
        # floor 확정
        self.CompliteLevel = 0
    def CoordinateInput(self,val):
        self.y = val
        self.y1 = self.y + (self.Right_Idle.h//2);self.y2 = self.y - (self.Right_Idle.h//2)
    def WallCrash(self): # 벽에 부딪히면 호출
        global xPos
        self.x -= xPos * 4 ; self.x1 -= xPos * 4; self.x2 -= xPos * 4

    def Player_Movement(self,floors,walls):
        global MoveRight , MoveLeft ,xPos,yPos,frame,FALLING,dir,JUMPKEYDOWN
        global play

        if(JUMPKEYDOWN == False):
            if(MoveRight == True and MoveLeft == False):
                frame += 1
                self.Right_Run.clip_draw(((frame//2) % 10)*(self.Right_Run.w//10), 0, self.Right_Run.w//10, self.Right_Run.h,self.x,self.y)
                delay(0.01)
            elif(MoveRight == False and MoveLeft == True):
                frame += 1
                self.Left_Run.clip_draw(((frame//2) % 10)*(self.Left_Run.w//10), 0, self.Left_Run.w//10, self.Left_Run.h,self.x,self.y)
                delay(0.01)
            elif(MoveRight == False and MoveLeft == False):
                frame += 1
                if(dir == 0):
                    self.Right_Idle.clip_draw(((frame//5) % 7)*(self.Right_Idle.w//7), 0,self.Right_Idle.w//7,self.Right_Idle.h,self.x,self.y)
                else :
                    self.Left_Idle.clip_draw(((frame//5) % 7)*(self.Left_Idle.w//7), 0,self.Left_Idle.w//7,self.Left_Idle.h,self.x,self.y)
                delay(0.01)
        elif (JUMPKEYDOWN == True):
            if FALLING == False: # 점프로 올라가는 애니메이션
                if dir == 0: 
                    if(yPos > (JUMPHEIGHT /3)*2): # 점프 모션을 3분할 하여 더욱 자연스럽게 직관적으로.
                        self.Right_Jump.clip_draw(0*(self.Right_Jump.w//3), 0,self.Right_Jump.w//3,self.Right_Jump.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)):
                        self.Right_Jump.clip_draw(1*(self.Right_Jump.w//3), 0,self.Right_Jump.w//3,self.Right_Jump.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)*0):
                        self.Right_Jump.clip_draw(2*(self.Right_Jump.w//3), 0,self.Right_Jump.w//3,self.Right_Jump.h,self.x,self.y)
                elif dir == 1:
                    if(yPos > (JUMPHEIGHT /3)*2):
                        self.Left_Jump.clip_draw(0*(self.Left_Jump.w//3), 0,self.Left_Jump.w//3,self.Left_Jump.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)):
                        self.Left_Jump.clip_draw(1*(self.Left_Jump.w//3), 0,self.Left_Jump.w//3,self.Left_Jump.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)*0):
                        self.Left_Jump.clip_draw(2*(self.Left_Jump.w//3), 0,self.Left_Jump.w//3,self.Left_Jump.h,self.x,self.y)
                
            elif FALLING == True: # 점프 이후 떨어지는 애니메이션
                if dir == 0: 
                    if(yPos > (JUMPHEIGHT /3)*2): # 하강 모션을 3분할 하여 더욱 자연스럽게 직관적으로.
                        self.Right_Fall.clip_draw(0*(self.Right_Fall.w//3), 0,self.Right_Fall.w//3,self.Right_Fall.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)):
                        self.Right_Fall.clip_draw(1*(self.Right_Fall.w//3), 0,self.Right_Fall.w//3,self.Right_Fall.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)*0):
                        self.Right_Fall.clip_draw(2*(self.Right_Fall.w//3), 0,self.Right_Fall.w//3,self.Right_Fall.h,self.x,self.y)    
                elif dir == 1:
                    if(yPos > (JUMPHEIGHT /3)*2):
                        self.Left_Fall.clip_draw(2*(self.Left_Fall.w//3), 0,self.Left_Fall.w//3,self.Left_Fall.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)):
                        self.Left_Fall.clip_draw(1*(self.Left_Fall.w//3), 0,self.Left_Fall.w//3,self.Left_Fall.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)*0):
                        self.Left_Fall.clip_draw(0*(self.Left_Fall.w//3), 0,self.Left_Fall.w//3,self.Left_Fall.h,self.x,self.y)
            delay(0.01)
        
        # player 좌표 이동
        self.x += xPos * 4
        self.x1 += xPos * 4; self.x2 += xPos * 4
        if self.x2 > GameWindow_WITDH or self.x1 < 0: 
            self.WallCrash()
        # enumerate 는 리스트의 인덱스,원소 형식의 튜플을 넘김
        for idx,wall in enumerate(walls):
            wall.Crash(self,idx)
        if self.Wallpoint >= 0 and not JUMPKEYDOWN: # 벽위에 올라갔을때 해당 벽에서 멀어지면 떨어짐.
            if ((self.x2 + self.x1)//2 < walls[self.Wallpoint].x1 or 
            (self.x2 + self.x1)//2 > walls[self.Wallpoint].x2):
                JUMPKEYDOWN =True; FALLING =True ;yPos = JUMPHEIGHT
                self.Wallpoint = -1
        if JUMPKEYDOWN :
            if FALLING == False: # 점프로 올라가는 애니메이션
                self.y += yPos ; self.y1 += yPos ;self.y2 += yPos 
                # 점프로 올라갈때 벽에 부딪히면 못올라가게.
                if (self.level+1 < len(floors)):
                    if(floors[self.level+1].y2 < self.y + self.Right_Jump.h//2 
                    and floors[self.level+1].y1 > self.y + self.Right_Jump.h//2 
                    and floors[self.level+1].x1 < self.x and floors[self.level+1].x2 > self.x):
                        self.y -= yPos;self.y1 -= yPos ;self.y2 -= yPos 
            elif FALLING == True: # 점프 이후 떨어지는 애니메이션
                if yPos <= JUMPHEIGHT : # 체공 시간 이후 떨어지게
                    self.y -= yPos ; self.y1 -= yPos ;self.y2 -= yPos
                    # 떨어질때 floor를 밟음.
                    if (self.level+1 < len(floors)):
                        if (floors[self.level+1].y2 < self.y - self.Right_Idle.h//2 
                        and floors[self.level+1].y1 > self.y - self.Right_Idle.h//2 
                        and floors[self.level+1].x1 < self.x and floors[self.level+1].x2 > self.x):
                            self.y = floors[self.level+1].y1 + self.Right_Idle.h//2
                            self.y1 = self.y + (self.Right_Idle.h//2)
                            self.y2 = self.y - (self.Right_Idle.h//2)
                            yPos = 1
                            # Floor 레벨 동일 적용 플레이어가 위치한 발판의 인덱스
                            self.level = self.level + 1
                            self.CompliteLevel = self.level
                    if (floors[self.level].y2 < self.y - self.Right_Idle.h//2 
                    and floors[self.level].y1 > self.y - self.Right_Idle.h//2 
                    and floors[self.level].x1 < self.x and floors[self.level].x2 > self.x):
                        # self.y += yPos ; self.y1 += yPos ;self.y2 += yPos
                        self.y = floors[self.level].y1 + self.Right_Idle.h//2
                        self.y1 = self.y + (self.Right_Idle.h//2)
                        self.y2 = self.y - (self.Right_Idle.h//2)
                        yPos = 1
                        self.CompliteLevel = self.level
                    if (self.level != 0):
                        if (floors[self.level-1].y2 < self.y - self.Right_Idle.h//2 
                        and floors[self.level-1].y1 > self.y - self.Right_Idle.h//2 
                        and floors[self.level-1].x1 < self.x and floors[self.level-1].x2 > self.x):
                            # self.y += yPos ; self.y1 += yPos ;self.y2 += yPos
                            self.y = floors[self.level-1].y1 + self.Right_Idle.h//2
                            self.y1 = self.y + (self.Right_Idle.h//2)
                            self.y2 = self.y - (self.Right_Idle.h//2)
                            yPos = 1
                            self.level = self.level - 1
                            self.CompliteLevel = self.level
        
            yPos -= 1
            if(yPos == 0): # 첫 번째 ypos가 0이 되는 경우는 점프까 끝난상태 두번째는 떨어지는 상태 전환 
                if FALLING == True :
                    FALLING = False
                    JUMPKEYDOWN = False
                    # 현재 floor의 밖에 있다 (떨어져야함)
                    if(floors[self.level].x1 > self.x + (self.Right_Run.w//10)//2 
                    or floors[self.level].x2 < self.x - (self.Right_Run.w//10)//2):
                        JUMPKEYDOWN , FALLING = True , True
                        yPos = JUMPHEIGHT
                        self.y -= yPos ; self.y1 -= yPos ;self.y2 -= yPos
                        yPos -= 1
                        self.level -= 1
                    else:
                        # 같은 레벨에 floor로 떨어지는데 그 레벨에 맞지 않는 높이라면 더욱 떨어지게
                        if (floors[self.level].y1 + 5 < self.y2):
                            JUMPKEYDOWN , FALLING = True , True
                            yPos = JUMPHEIGHT
                            self.y -= yPos ; self.y1 -= yPos ;self.y2 -= yPos
                            yPos -= 1
                        self.CompliteLevel = self.level
                else :
                    FALLING = True
                    yPos = JUMPHEIGHT + 7 # + 7 은 공중에서 체공하는 시간정도를 나타냄.
        elif (not JUMPKEYDOWN and self.Wallpoint == -1) : # JUMPKEYDOWN 이 False 일때 벽위에 있지 않을때
            if(floors[self.level].x1 > self.x + (self.Right_Run.w//10)//2 
            or floors[self.level].x2 < self.x - (self.Right_Run.w//10)//2):
                JUMPKEYDOWN , FALLING = True , True
                yPos = JUMPHEIGHT
                self.level -= 1


MoveRight ,MoveLeft = False , False

FALLING = False
frame = 0

xPos , yPos = 0,0

# dir 0 이면 오른쪽 1 이면 왼쪽을 마지막에 봄.
dir = 0
play = True

# 순서대로 방향키 좌, 우 누르면 1 때면 0
Current_KeyDown_List = [0,0]


# 현재 다른 키와 같이 눌려있는지 상태 확인 하나만 눌려있으면 idle 상태로
def Current_KeyDown_Status():
    global Current_KeyDown_List , MoveRight ,MoveLeft
    temp = 0
    for i in Current_KeyDown_List:
        if i == 1:
            temp +=1
    if temp == 1 :
        MoveRight ,MoveLeft = False ,False
 
import FloorObject
import WallObject
floortype = 1 # map tool variable
tool_name = 'floor' # map tool type

def KeyDown_event(floors,player,walls): # map tool variable
    global play , xPos , yPos ,MoveLeft ,MoveRight ,dir,JUMPKEYDOWN, FALLING,Current_KeyDown_List
    global floortype , tool_name
    events = get_events()

    for event in events:
        if(event.type == SDL_QUIT or event.key == SDLK_ESCAPE):
            play = False
            # map tool start
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if tool_name == 'floor':
                floors += [FloorObject.FLOOR(event.x,600-event.y,floortype)]
            elif tool_name == 'wall':
                walls += [WallObject.WALL(event.x,600-event.y)]
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
            if tool_name == 'floor':
                if floors[-1].level != player.level:
                    floors.pop(len(floors)-1)
                    FloorObject.level -= 1
            elif tool_name == 'wall':
                if(len(walls)> 0):
                    walls.pop(len(walls)-1)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1: # 현재 플로어 정보 출력
            print('\nx 좌표 출력')
            for floor in floors:
                print(floor.xPos,end = ',')
            print('\ny 좌표 출력')
            for floor in floors:
                print(floor.yPos+(100*player.level),end = ',')
            print('\n이미지 타입 출력')
            for floor in floors:
                print(floor.floortype,end = ',') 
            print('\n') # map tool end
        elif (event.type == SDL_KEYDOWN):
            if(event.key == SDLK_RIGHT):
                MoveRight ,MoveLeft = True ,False
                dir = 0
                Current_KeyDown_List[0] = 1
                xPos += 1
            if(event.key == SDLK_LEFT):
                MoveRight ,MoveLeft = False , True
                dir = 1
                Current_KeyDown_List[1] = 1
                xPos -= 1
            if(event.key == SDLK_SPACE):
                if yPos != 0:
                    continue
                yPos = JUMPHEIGHT
                JUMPKEYDOWN = True
        elif (event.type == SDL_KEYUP):
            if(event.key == SDLK_RIGHT):
                Current_KeyDown_Status()
                Current_KeyDown_List[0] = 0
                if Current_KeyDown_List[1] == 1 :
                    MoveRight ,MoveLeft = False , True
                xPos -= 1
            if(event.key == SDLK_LEFT):
                Current_KeyDown_Status()
                Current_KeyDown_List[1] = 0
                if Current_KeyDown_List[0] == 1 :
                    MoveRight ,MoveLeft = True , False
                xPos += 1