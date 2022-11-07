from pico2d import *

class SKILL:
    def __init__(self):
        # 스킬 쿨타임
        self.cooltime = [0,0,0]
        self.skill_state = [None,None,None]
        # 시간정지 시간
        self.skill_timestop_duration = 500
        # 무적 시간
        self.nodamegetime = 0
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
        self.cooltime[1] = 1000
        self.nodamegetime = 300
        self.skill_state[1] = 'godmod'

    def skill_explosion(self):
        print("explosion")
        self.cooltime[2] = 100
        self.skill_state[2] = 'explosion'

    def update(self):
        self.skill_timestop_update()
        # 스킬을 사용하면 쿨타임이 생기고 쿨타임을 update 마다 1씩 줄임
        for index,cooltime in enumerate(self.cooltime):
            if cooltime != 0:
                # print(cooltime)
                self.cooltime[index] -= 1
        if self.nodamegetime != 0 : self.nodamegetime -= 1
