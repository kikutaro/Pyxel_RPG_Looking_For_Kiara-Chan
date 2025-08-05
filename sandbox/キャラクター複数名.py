import pyxel
import os
import sys
sys.path.append(os.getcwd())
import const
from model.character import Character
from model.main_character import MainCharacter

class キャラクター複数名:
    def __init__(self):
        pyxel.init(const.L_WIDTH,const.L_HEIGHT,"Character")
        pyxel.load('../my_resource.pyxres')

        self.maika = MainCharacter(232*8,60,"まいか")
        self.members = [
            Character(20,80,"りさ"),
            Character(100,100,"あんな"),
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        self.maika.update(self.members)
        for member in self.members:
            member.update()

    def draw(self):
        pyxel.cls(7)
        pyxel.bltm(
            0,0,
            0,
            232 * 8, 0,
            const.L_WIDTH,const.L_HEIGHT)
        self.maika.draw()

        for member in self.members:
            member.draw()

キャラクター複数名()