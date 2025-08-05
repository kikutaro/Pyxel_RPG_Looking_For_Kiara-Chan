import pyxel
from キャラクター import キャラクター

class 実行:
    def __init__(self):
        pyxel.init(128,128,"キャラクター当たり判定")
        pyxel.load('../../my_resource.pyxres')

        self.まいか = キャラクター(0,0,"まいか")
        self.きあら = キャラクター(100,100,"きあら")

        pyxel.run(self.update, self.draw)

    def update(self):
        self.まいか.移動()
        if self.まいか.他のキャラクターと接触したかどうか(self.きあら):
            print(pyxel.frame_count , "接触した...！")

    def draw(self):
        pyxel.cls(7)
        pyxel.blt(self.まいか.x座標,self.まいか.y座標,0,64,0,16,16)
        pyxel.blt(self.きあら.x座標,self.きあら.y座標,0,144,64,16,16)

実行()