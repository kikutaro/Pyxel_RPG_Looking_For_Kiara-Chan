import pyxel
import const

class Gameclear:
    def __init__(self, rpg):
        self.rpg = rpg
        self.h = const.FIELD

    def start(self):
        pass
    
    def update(self):
        if self.h > const.FIELD / 2 - 20:
            self.h -= 1

    def draw(self):
        pyxel.cls(const.色.WHITE.value)
        pyxel.text(40,self.h,"Created By イコまい", const.色.BLACK.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
        pyxel.text(40,self.h + 10,"Please visit https://equal-maika.jp", const.色.BLACK.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
        pyxel.blt(40,self.h+20,0,
                        160,80,
                        const.キャラサイズ,const.キャラサイズ, const.色.WHITE.value)