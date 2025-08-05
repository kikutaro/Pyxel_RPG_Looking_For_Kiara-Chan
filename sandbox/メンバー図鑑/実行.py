import pyxel
import os
import sys
sys.path.append(os.getcwd())
import const

class メンバー紹介:
    def __init__(self):
        print(list(const.キャラ.keys()))

    def update(self):
        pass

    def draw(self):
        pass

メンバー紹介()