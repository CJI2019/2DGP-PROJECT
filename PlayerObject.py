from pico2d import *
import game_framework as gf
import Main
GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600
# 점프 높이
JUMPHEIGHT = 0.17

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
        self.Right_Crash = load_image('Player\Player_right_crash.png')
        self.Left_Crash = load_image('Player\Player_left_crash.png')

        self.Right_key = load_image('left_key.png')
        self.Left_key = load_image('right_key.png')
        self.x = 300
        self.y = 300
        self.dir = 1
        # 좌 상
        self.x1, self.y1 = self.x - (self.Right_Idle.w//8//2), self.y + (self.Right_Idle.h//2)
        # 우 하
        self.x2, self.y2 = self.x + (self.Right_Idle.w//8//2), self.y - (self.Right_Idle.h//2)
        self.Wallpoint = -1
        # 현재 floor 판별
        self.level = 0
        # floor 확정
        self.CompliteLevel = 0
        self.status = None
        self.stoptime = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
    def get_bb(self):
        return self.x1,self.y1,self.x2,self.y2
    def CoordinateInput(self,val):
        self.y = val
        self.y1 = self.y + (self.Right_Idle.h//2);self.y2 = self.y - (self.Right_Idle.h//2)
    def WallCrash(self,frame_time): # 벽 장애물에 부딪히면 호출
        global xPos
        self.x -= xPos * RUN_SPEED_PPS * frame_time
        self.x1 -= xPos * RUN_SPEED_PPS * frame_time
        self.x2 -= xPos * RUN_SPEED_PPS * frame_time
    def MonsterCrash(self,monster): # 몬스터와 충돌
        global MoveRight,MoveLeft , xPos
        if Main.Skill.nodamegetime >= 0: return
        if (monster.x1 < self.x and self.x < monster.x2 and monster.y2 < self.y and self.y < monster.y1):
            if(self.stoptime == 0):
                print('몬스터 충돌')
                self.status = 'monstercrash' ; self.stoptime = 20
    def draw(self):
        global MoveRight, MoveLeft,xPos,yPos,frame,FALLING,JUMPKEYDOWN
        global play
        if self.status == 'monstercrash':
            if (self.dir == 1):
                self.Right_key.draw(self.x,self.y+(self.Right_Run.h//2))
                self.Right_Crash.draw(self.x,self.y-(self.Right_Run.h//4))
            elif (self.dir == -1):
                self.Left_key.draw(self.x,self.y+(self.Right_Run.h//2))
                self.Left_Crash.draw(self.x,self.y-(self.Right_Run.h//4))
        elif(JUMPKEYDOWN == False):
            if xPos == 1:
                frame = (frame + RUN_FRAMES_PER_ACTION * ACTION_PER_TIME * gf.frame_time) % RUN_FRAMES_PER_ACTION
                self.Right_Run.clip_draw(int(frame)*(self.Right_Run.w//10), 0, self.Right_Run.w//10, self.Right_Run.h,self.x,self.y)
            elif xPos == -1:
                frame = (frame + RUN_FRAMES_PER_ACTION * ACTION_PER_TIME * gf.frame_time) % RUN_FRAMES_PER_ACTION
                self.Left_Run.clip_draw(int(frame)*(self.Left_Run.w//10), 0, self.Left_Run.w//10, self.Left_Run.h,self.x,self.y)
            elif xPos == 0:
                frame = (frame + IDLE_FRAMES_PER_ACTION * IDLE_ACTION_PER_TIME * gf.frame_time) % IDLE_FRAMES_PER_ACTION
                if self.dir == 1:
                    self.Right_Idle.clip_draw(int(frame)*(self.Right_Idle.w//7), 0,self.Right_Idle.w//7,self.Right_Idle.h,self.x,self.y)
                elif self.dir == -1:
                    self.Left_Idle.clip_draw(int(frame)*(self.Left_Idle.w//7), 0,self.Left_Idle.w//7,self.Left_Idle.h,self.x,self.y)
        elif (JUMPKEYDOWN == True):
            if FALLING == False: # 점프로 올라가는 애니메이션
                if self.dir == 1:
                    if(yPos > (JUMPHEIGHT /3)*2): # 점프 모션을 3분할 하여 더욱 자연스럽게 직관적으로.
                        self.Right_Jump.clip_draw(0*(self.Right_Jump.w//3), 0,self.Right_Jump.w//3,self.Right_Jump.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)):
                        self.Right_Jump.clip_draw(1*(self.Right_Jump.w//3), 0,self.Right_Jump.w//3,self.Right_Jump.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)*0):
                        self.Right_Jump.clip_draw(2*(self.Right_Jump.w//3), 0,self.Right_Jump.w//3,self.Right_Jump.h,self.x,self.y)
                elif self.dir == -1:
                    if(yPos > (JUMPHEIGHT /3)*2):
                        self.Left_Jump.clip_draw(0*(self.Left_Jump.w//3), 0,self.Left_Jump.w//3,self.Left_Jump.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)):
                        self.Left_Jump.clip_draw(1*(self.Left_Jump.w//3), 0,self.Left_Jump.w//3,self.Left_Jump.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)*0):
                        self.Left_Jump.clip_draw(2*(self.Left_Jump.w//3), 0,self.Left_Jump.w//3,self.Left_Jump.h,self.x,self.y)
            elif FALLING == True: # 점프 이후 떨어지는 애니메이션
                if self.dir == 1:
                    if(yPos > (JUMPHEIGHT /3)*2): # 하강 모션을 3분할 하여 더욱 자연스럽게 직관적으로.
                        self.Right_Fall.clip_draw(0*(self.Right_Fall.w//3), 0,self.Right_Fall.w//3,self.Right_Fall.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)):
                        self.Right_Fall.clip_draw(1*(self.Right_Fall.w//3), 0,self.Right_Fall.w//3,self.Right_Fall.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)*0):
                        self.Right_Fall.clip_draw(2*(self.Right_Fall.w//3), 0,self.Right_Fall.w//3,self.Right_Fall.h,self.x,self.y)    
                elif self.dir == -1:
                    if(yPos > (JUMPHEIGHT /3)*2):
                        self.Left_Fall.clip_draw(2*(self.Left_Fall.w//3), 0,self.Left_Fall.w//3,self.Left_Fall.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)):
                        self.Left_Fall.clip_draw(1*(self.Left_Fall.w//3), 0,self.Left_Fall.w//3,self.Left_Fall.h,self.x,self.y)
                    elif (yPos > (JUMPHEIGHT /3)*0):
                        self.Left_Fall.clip_draw(0*(self.Left_Fall.w//3), 0,self.Left_Fall.w//3,self.Left_Fall.h,self.x,self.y)
        
    # player 좌표 이동
    def update(self):
        global MoveRight, MoveLeft, xPos, yPos, frame, FALLING, JUMPKEYDOWN
        global play

        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)
            print('event')

        # enumerate 는 리스트의 인덱스,원소 형식의 튜플을 넘김
        for idx,wall in enumerate(Main.walls):
            wall.Crash(self,idx,gf.frame_time)
        if self.Wallpoint >= 0 and not JUMPKEYDOWN: # 벽위에 올라갔을때 해당 벽에서 멀어지면 떨어짐.
            if ((self.x2 + self.x1)//2 < Main.walls[self.Wallpoint].x1 or
            (self.x2 + self.x1)//2 > Main.walls[self.Wallpoint].x2):
                JUMPKEYDOWN =True; FALLING =True ;yPos = JUMPHEIGHT
                self.Wallpoint = -1
        if JUMPKEYDOWN:
            if FALLING == False: # 점프로 올라가는 애니메이션
                self.y += JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                self.y1 += JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                self.y2 += JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                # 점프로 올라갈때 벽에 부딪히면 못올라가게.
                if (self.level+1 < len(Main.floors)):
                    if(Main.floors[self.level+1].y2 < self.y + self.Right_Jump.h//2
                    and Main.floors[self.level+1].y1 > self.y + self.Right_Jump.h//2
                    and Main.floors[self.level+1].x1 < self.x and Main.floors[self.level+1].x2 > self.x):
                        self.y -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                        self.y1 -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                        self.y2 -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
            elif FALLING == True: # 점프 이후 떨어지는 애니메이션
                if yPos <= JUMPHEIGHT : # 체공 시간 이후 떨어지게
                    self.y -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                    self.y1 -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                    self.y2 -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                    # 떨어질때 floor를 밟음.
                    if (self.level+1 < len(Main.floors)):
                        if (Main.floors[self.level+1].y2 < self.y - self.Right_Idle.h//2
                        and Main.floors[self.level+1].y1 > self.y - self.Right_Idle.h//2
                        and Main.floors[self.level+1].x1 < self.x and Main.floors[self.level+1].x2 > self.x):
                            self.y = Main.floors[self.level+1].y1 + self.Right_Idle.h//2
                            self.y1 = self.y + (self.Right_Idle.h//2)
                            self.y2 = self.y - (self.Right_Idle.h//2)
                            yPos = 0
                            # Floor 레벨 동일 적용 플레이어가 위치한 발판의 인덱스
                            self.level = self.level + 1
                            self.CompliteLevel = self.level
                    if (Main.floors[self.level].y2 < self.y - self.Right_Idle.h//2
                    and Main.floors[self.level].y1 > self.y - self.Right_Idle.h//2
                    and Main.floors[self.level].x1 < self.x and Main.floors[self.level].x2 > self.x):
                        # self.y += yPos ; self.y1 += yPos ;self.y2 += yPos
                        self.y = Main.floors[self.level].y1 + self.Right_Idle.h//2
                        self.y1 = self.y + (self.Right_Idle.h//2)
                        self.y2 = self.y - (self.Right_Idle.h//2)
                        yPos = 0
                        self.CompliteLevel = self.level
                    if (self.level != 0):
                        if (Main.floors[self.level-1].y2 < self.y - self.Right_Idle.h//2
                        and Main.floors[self.level-1].y1 > self.y - self.Right_Idle.h//2
                        and Main.floors[self.level-1].x1 < self.x and Main.floors[self.level-1].x2 > self.x):
                            # self.y += yPos ; self.y1 += yPos ;self.y2 += yPos
                            self.y = Main.floors[self.level-1].y1 + self.Right_Idle.h//2
                            self.y1 = self.y + (self.Right_Idle.h//2)
                            self.y2 = self.y - (self.Right_Idle.h//2)
                            yPos = 0
                            self.level = self.level - 1
                            self.CompliteLevel = self.level
            yPos -= gf.frame_time
            if(yPos <= 0): # 첫 번째 ypos가 0이 되는 경우는 점프까 끝난상태 두번째는 떨어지는 상태 전환
                if FALLING == True :
                    FALLING = False
                    JUMPKEYDOWN = False
                    # 현재 floor의 밖에 있다 (떨어져야함)
                    if(Main.floors[self.level].x1 > self.x + (self.Right_Run.w//10)//2
                    or Main.floors[self.level].x2 < self.x - (self.Right_Run.w//10)//2):
                        JUMPKEYDOWN , FALLING = True , True
                        yPos = JUMPHEIGHT
                        self.y -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                        self.y1 -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                        self.y2 -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                        yPos -= gf.frame_time
                        self.level -= 1
                    else:
                        # 같은 레벨에 floor로 떨어지는데 그 레벨에 맞지 않는 높이라면 더욱 떨어지게
                        if (Main.floors[self.level].y1 + 5 < self.y2):
                            JUMPKEYDOWN , FALLING = True , True
                            yPos = JUMPHEIGHT
                            self.y -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                            self.y1 -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                            self.y2 -= JUMP_SPEED * RUN_SPEED_PPS * gf.frame_time
                            yPos -= gf.frame_time
                        self.CompliteLevel = self.level
                else :
                    FALLING = True
                    yPos = JUMPHEIGHT + 0.15# + 7 은 공중에서 체공하는 시간정도를 나타냄.
        elif (not JUMPKEYDOWN and self.Wallpoint == -1) : # JUMPKEYDOWN 이 False 일때 벽위에 있지 않을때
            if(Main.floors[self.level].x1 > self.x + (self.Right_Run.w//10)//2
            or Main.floors[self.level].x2 < self.x - (self.Right_Run.w//10)//2):
                JUMPKEYDOWN , FALLING = True , True
                yPos = JUMPHEIGHT
                self.level -= 1
    def handle_event(self, event):
        global yPos ,JUMPKEYDOWN
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
            print('event : ', key_event)

        elif event.type == SDL_KEYUP: return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if yPos > 0 or Main.Player.stoptime != 0:
                return
            yPos = JUMPHEIGHT
            JUMPKEYDOWN = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            Main.Potal.collision(self) # Game Clear
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            Main.Skill.skill_timestop()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            Main.Skill.skill_godmod()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            Main.Skill.skill_explosion(Main.monsters)
    def add_event(self, event):
        self.event_que.insert(0, event)

class IDLE:
    @staticmethod
    def enter(self,event):
        global xPos
        xPos = 0
        print('ENTER IDLE')
    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
    @staticmethod
    def do(self):
        pass
    @staticmethod
    def draw(self):
        pass
class RUN:
    def enter(self, event):
        global xPos
        print('ENTER RUN')
        if event == RD:
            xPos += 1
            if self.stoptime != 0:
                self.stoptime -= 1
                if self.stoptime == 0:
                    self.status = None
                    Main.Skill.nodamegetime = 1
        elif event == LD:
            xPos -= 1
            if self.stoptime != 0:
                self.stoptime -= 1
                if self.stoptime == 0:
                    self.status = None
                    Main.Skill.nodamegetime = 1
        elif event == RU:
            xPos -= 1
        elif event == LU:
            xPos += 1
    def exit(self, event):
        print('EXIT RUN')
        self.dir = xPos
    def do(self):
        if xPos != 0:
            self.dir = xPos

        if self.stoptime == 0:
            self.x += xPos * RUN_SPEED_PPS * gf.frame_time
            self.x = clamp(0+(self.Right_Idle.w//8//2),self.x,GameWindow_WITDH-(self.Right_Idle.w//8//2))
            self.x1 = self.x - (self.Right_Idle.w//8//2)
            self.x2 = self.x + (self.Right_Idle.w//8//2)
    def draw(self):
        pass

RD, LD, RU, LU = range(4)
event_name = ['RD', 'LD', 'RU', 'LU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},
}


PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KPH = 30 # km/h
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

JUMP_SPEED = 2.5

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
RUN_FRAMES_PER_ACTION = 8

IDLE_ACTION_PER_TIME = 1.0 / 0.5
IDLE_FRAMES_PER_ACTION = 7

MoveRight ,MoveLeft = False , False

FALLING = False
frame = 0

xPos , yPos = 0,0

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
 

def KeyDown_event(event): # map tool variable
    global  xPos , yPos ,MoveLeft ,MoveRight ,JUMPKEYDOWN, FALLING,Current_KeyDown_List
    events = get_events()

    if (event.type == SDL_KEYDOWN):
        if(event.key == SDLK_SPACE):
            if yPos > 0 or Main.Player.stoptime != 0:
                # continue
                return
            yPos = JUMPHEIGHT
            JUMPKEYDOWN = True
        elif (event.key == SDLK_UP):
            Main.Potal.collision(Main.Player) # Game Clear
        elif event.key == SDLK_a:
            Main.Skill.skill_timestop()
        elif event.key == SDLK_s:
            Main.Skill.skill_godmod()
        elif event.key == SDLK_d:
            Main.Skill.skill_explosion(Main.monsters)