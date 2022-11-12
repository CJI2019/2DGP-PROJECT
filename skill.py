from pico2d import *
from MonsterObject import explosionDeadmonsters
class SKILL:
    def __init__(self):
        # ui 스킬 이미지
        self.skill_timestop_ui_image = load_image('Skill/skill_timestop.png')
        self.skill_timestop_cooltime_ui_image = load_image('Skill/skill_timestop_cooltime.png')
        self.skill_godmod_ui_image = load_image('Skill/skill_godmod.png')
        self.skill_godmod_cooltime_ui_image = load_image('Skill/skill_godmod_cooltime.png')
        self.skill_explosion_ui_image = load_image('Skill/skill_explosion.png')
        self.skill_explosion_cooltime_ui_image = load_image('Skill/skill_explosion_cooltime.png')
        # 스킬 사용 애니메이션 이미지
        self.skill_timestop_anime = load_image('Skill/timestop.png')
        self.skill_godmod_anime = load_image('Skill/godmod.png')
        self.skill_explosion_anime = load_image('Skill/explosion.png')
        self.skill_explosion_frame = 0


        # 스킬 쿨타임
        self.cooltime = [0,0,0]
        self.skill_state = [None,None,None]
        # 시간정지 시간
        self.skill_timestop_duration = 500
        # 무적 시간
        self.nodamegetime = 0

    def draw(self,player):
        if(self.cooltime[0] == 0):
            self.skill_timestop_ui_image.clip_composite_draw(0,0,self.skill_timestop_ui_image.w,self.skill_timestop_ui_image.h,0,'',32,32,64,64)
        else:
            self.skill_timestop_cooltime_ui_image.clip_composite_draw(0,0,self.skill_timestop_cooltime_ui_image.w,self.skill_timestop_cooltime_ui_image.h,0,'',32,32,64,64)
        if (self.cooltime[1] == 0):
            self.skill_godmod_ui_image.clip_composite_draw(0, 0, self.skill_godmod_ui_image.w,self.skill_godmod_ui_image.h, 0, '', 96, 32, 64, 64)
        else:
            self.skill_godmod_cooltime_ui_image.clip_composite_draw(0, 0, self.skill_godmod_cooltime_ui_image.w,self.skill_godmod_cooltime_ui_image.h, 0, '', 96, 32, 64, 64)
        if (self.cooltime[2] == 0):
            self.skill_explosion_ui_image.clip_composite_draw(0, 0, self.skill_explosion_ui_image.w,self.skill_explosion_ui_image.h, 0, '', 160, 32, 64, 64)
        else:
            self.skill_explosion_cooltime_ui_image.clip_composite_draw(0, 0, self.skill_explosion_cooltime_ui_image.w,self.skill_explosion_cooltime_ui_image.h, 0, '', 160,32, 64, 64)

        if(self.skill_state[0] != None):
            self.skill_timestop_anime.draw(300,300)
        if (self.skill_state[1] != None):
            self.skill_godmod_anime.clip_composite_draw(0, 0, self.skill_godmod_anime.w,self.skill_godmod_anime.h, 0, '', player.x,player.y, 130, 130)
        if(self.skill_state[2] != None):
            self.skill_explosion_anime.clip_composite_draw(int(self.skill_explosion_frame)*int(self.skill_explosion_anime.w//7), 0, int(self.skill_explosion_anime.w//7),int(self.skill_explosion_anime.h), 0, '', 300,300, 600, 600)
    #   시간 정지 스킬 사용
    def skill_timestop(self):
        if self.cooltime[0] == 0:
            print("timestop")
            self.cooltime[0] = 1000
            self.skill_state[0] = 'timestop'
    def skill_timestop_update(self):
        if self.skill_state[0] != None:
            self.skill_timestop_duration -= 1
        if self.skill_timestop_duration == 0:
            print("timestop EXIT")
            self.skill_state[0] = None
            self.skill_timestop_duration = 500

    def skill_godmod(self):
        print("godmod")
        if self.cooltime[1] == 0:
            self.cooltime[1] = 1000
            self.nodamegetime = 300
            self.skill_state[1] = 'godmod'

    def skill_explosion(self,monsters):
        if self.cooltime[2] == 0:
            print("explosion")
            explosionDeadmonsters(monsters)
            self.cooltime[2] = 1000
            self.skill_state[2] = 'explosion'
            self.skill_explosion_frame = 0
    def update(self,frame_time):
        self.skill_timestop_update()
        # 스킬을 사용하면 쿨타임이 생기고 쿨타임을 update 마다 1씩 줄임
        for index,cooltime in enumerate(self.cooltime):
            if cooltime != 0: self.cooltime[index] -= 1
        if self.nodamegetime != 0 :
            self.nodamegetime -= 1
            if self.nodamegetime == 0:
                self.skill_state[1] = None
        if self.cooltime[2] != 0:
            self.skill_explosion_frame = (self.skill_explosion_frame + EXPLOSION_FRAMES_PER_ACTION * EXPLOSION_ACTION_PER_TIME * frame_time) % EXPLOSION_FRAMES_PER_ACTION
            if self.skill_explosion_frame >= 6.5:
                self.skill_state[2] = None


EXPLOSION_ACTION_PER_TIME = 1.0 / 0.5
EXPLOSION_FRAMES_PER_ACTION = 7