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

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x座標, self.y座標, 0, 0, 0, 16, 16)

    def 他のキャラクターと接触したかどうか(self, 他のキャラクター):
        if self.x座標 < 他のキャラクター.x座標 + 16 and self.x座標 + 16 > 他のキャラクター.x座標 and self.y座標 < 他のキャラクター.y座標 + 16 and self.y座標 + 16 > 他のキャラクター.y座標:
            return True
        return False
    
    def 他のキャラクターと接触するかどうか(self, 次のx座標, 次のy座標, 他のキャラクター):
        if 次のx座標 < 他のキャラクター.x座標 + 16 and 次のx座標 + 16 > 他のキャラクター.x座標 and 次のy座標 < 他のキャラクター.y座標 + 16 and 次のy座標 + 16 > 他のキャラクター.y座標:
            return True
        return False
    
    def 次の移動で他のキャラクターと接触するかどうか(self, 他のキャラクター):
        if pyxel.btn(pyxel.KEY_LEFT):
            if not self.他のキャラクターと接触するかどうか(self.x座標 - self.移動距離, self.y座標, 他のキャラクター):
                self.x座標 -= self.移動距離
        if pyxel.btn(pyxel.KEY_RIGHT):
            if not self.他のキャラクターと接触するかどうか(self.x座標 + self.移動距離, self.y座標, 他のキャラクター):
                self.x座標 += self.移動距離
        if pyxel.btn(pyxel.KEY_UP):
            if not self.他のキャラクターと接触するかどうか(self.x座標 , self.y座標 - self.移動距離,他のキャラクター):
                self.y座標 -= self.移動距離
        if pyxel.btn(pyxel.KEY_DOWN):
            if not self.他のキャラクターと接触するかどうか(self.x座標 , self.y座標 + self.移動距離, 他のキャラクター):
                self.y座標 += self.移動距離
        