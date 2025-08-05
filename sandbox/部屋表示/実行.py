import pyxel
import os
import sys
sys.path.append(os.getcwd())
import const
from model.main_character import MainCharacter

class 実行:
    def __init__(self):
        pyxel.init(const.L_WIDTH, const.L_HEIGHT,"部屋表示")
        pyxel.load('../../my_resource.pyxres')

        self.まいか = MainCharacter(80,80,80,80,"まいか")

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        self.マップ更新(self.まいか.local_x, self.まいか.local_y)
        self.まいか.draw()
        pyxel.rect(10,10, 30, 20, const.色.YELLOW.value)
        pyxel.text(12,12, "楽屋", const.色.BLACK.value,const.MESSAGE_FONT)

    def マップ更新(self,x座標,y座標):
        pyxel.cls(7)
        描画マップx = (x座標 + 16) // 256 * 256
        描画マップy = (y座標 + 16) // 256 * 256 
        pyxel.bltm(0,0,0, 描画マップx, 描画マップy, 256,256)

実行()