import pyxel
from キャラクター import キャラクター

class 実行:
    def __init__(self):
        pyxel.init(256,256,"マップ移動")
        pyxel.load('../../my_resource.pyxres')

        self.まいか = キャラクター(0,0,0,0,"まいか",self)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.まいか.移動()

    def draw(self):
        self.マップ更新(self.まいか.グローバルx座標, self.まいか.グローバルy座標)
        self.まいか.draw()

    def マップ更新(self,x座標,y座標):
        pyxel.cls(7)
        描画マップx = (x座標 + 16) // 256 * 256
        描画マップy = (y座標 + 16) // 256 * 256 
        pyxel.bltm(0,0,0, 描画マップx, 描画マップy, 256,256)

実行()