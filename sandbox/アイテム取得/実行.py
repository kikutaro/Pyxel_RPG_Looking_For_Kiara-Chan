import pyxel
from キャラクター import キャラクター

class 実行:
    def __init__(self):
        pyxel.init(256,256,"アイテム取得")
        pyxel.load('../../my_resource.pyxres')

        self.まいか = キャラクター(0,0,"まいか")

        pyxel.run(self.update, self.draw)

    def update(self):
        self.まいか.移動()

    def draw(self):
        pyxel.cls(7)
        pyxel.blt(self.まいか.x座標,self.まいか.y座標,0,0,0,16,16)
        #メガホン\\\
        pyxel.blt(80,80,1,176,32,16,16)
        
        map = pyxel.tilemaps[0].pget(self.まいか.x座標 // 16, self.まいか.y座標 // 16)
        print(map)
実行()