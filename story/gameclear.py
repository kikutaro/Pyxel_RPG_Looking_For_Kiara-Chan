import pyxel
import const

class Gameclear:
    def __init__(self, rpg):
        self.rpg = rpg
        self.h = const.FIELD

    def start(self):
        pass
    
    def update(self):
        if self.h > 70:
            self.h -= 1

        if (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.KEY_RETURN)):
            pyxel.reset()

    def draw(self):
        pyxel.cls(const.色.WHITE.value)
        pyxel.text(40,self.h,"Created By イコまい (＠equal_maika_121)", const.色.BLACK.value, self.rpg.m_font)
        pyxel.text(40,self.h+10,"", const.色.WHITE.value)
        pyxel.text(40,self.h+20,"", const.色.WHITE.value)
        pyxel.text(40,self.h+30,"佐々木舞香ちゃん応援サイト", const.色.BLACK.value, self.rpg.m_font)
        pyxel.text(40,self.h+40,"https://equal-maika.jp", const.色.BLACK.value, self.rpg.m_font)
        pyxel.text(40,self.h+50,"", const.色.WHITE.value)
        pyxel.text(40,self.h+60,"", const.色.WHITE.value)
        pyxel.text(40,self.h+70,"きあらちゃんをさがせ / きあさが", const.色.BLACK.value, self.rpg.m_font)
        pyxel.text(40,self.h+80,"https://kiasaga.love", const.色.BLACK.value, self.rpg.m_font)
        pyxel.text(40,self.h+90,"ゲームの感想をおしえてね！", const.色.BLACK.value, self.rpg.m_font)

        pyxel.blt(40,self.h+100,0,
                        160,80,
                        const.キャラサイズ,const.キャラサイズ, const.色.WHITE.value)