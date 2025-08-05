import pyxel
import const
import random

class Profile:
    def __init__(self):
        self.members

    def メンバー追加(self, 名前, 血液型, 身長, 生年月日, 出身地, 趣味, 特技):
        member = {
            "名前": 名前,
            "血液型": 血液型,
            "身長": 身長,
            "生年月日": 生年月日,
            "出身地": 出身地,
            "趣味": 趣味,
            "特技": 特技
        }
        self.members.append(member)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "メンバー紹介", 7, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
        pyxel.rectb(10, 35, 80, 20, 7)
        pyxel.rectb(10, 65, 80, 80, 7)
        pyxel.rectb(100, 35, 146, 110, 7)
        pyxel.rectb(10, 155, 236, 80, 7)