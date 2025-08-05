import pyxel

class キャラクター:
    def __init__(self, ローカルx座標, ローカルy座標, グローバルx座標, グローバルy座標, 名前, ゲーム):
        self.ローカルx座標 = ローカルx座標
        self.ローカルy座標 = ローカルy座標
        self.グローバルx座標 = グローバルx座標
        self.グローバルy座標 = グローバルy座標
        self.名前 = 名前
        self.ゲーム = ゲーム
        self.移動距離 = 3

    def 移動(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.ローカルx座標 -= self.移動距離
            self.グローバルx座標 -= self.移動距離
            if self.ローカルx座標 < 0 and self.グローバルx座標 > 0:
                 self.ローカルx座標 = 240
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.ローカルx座標 += self.移動距離
            self.グローバルx座標 += self.移動距離
            if (self.ローカルx座標 + 16) / 256 > 1:
                 self.ローカルx座標 = 0
        if pyxel.btn(pyxel.KEY_UP):
            self.ローカルy座標 -= self.移動距離
            self.グローバルy座標 -= self.移動距離
            if self.ローカルy座標 < 0 and self.グローバルy座標 > 0:
                 self.ローカルy座標 = 240
        if pyxel.btn(pyxel.KEY_DOWN):
            self.ローカルy座標 += self.移動距離
            self.グローバルy座標 += self.移動距離
            if (self.ローカルy座標 + 16) / 256 > 1:
                 self.ローカルy座標 = 0

        print(self.ローカルx座標, self.ローカルy座標,self.グローバルx座標, self.グローバルy座標)

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.ローカルx座標, self.ローカルy座標, 0, 0, 0, 16, 16)