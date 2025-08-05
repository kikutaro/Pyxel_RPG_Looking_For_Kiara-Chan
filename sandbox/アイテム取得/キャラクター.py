import pyxel

class キャラクター:
    def __init__(self, x座標, y座標, 名前):
        self.x座標 = x座標
        self.y座標 = y座標
        self.name = 名前
        self.移動距離 = 3

    def 移動(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x座標 -= self.移動距離
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x座標 += self.移動距離
        if pyxel.btn(pyxel.KEY_UP):
            self.y座標 -= self.移動距離
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y座標 += self.移動距離

        self.update()

    def update(self):
        print(pyxel.tilemaps[0].pget(self.x座標//8 ,self.y座標//8))

    def draw(self):
        pyxel.blt(self.x座標, self.y座標, 0, 0, 0, 16, 16)

        