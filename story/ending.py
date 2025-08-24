import pyxel
import const
from model.character import Character
from model.message import Message

class Ending:
    def __init__(self, rpg):
        self.rpg = rpg
        self.messanger = None

        self.members = [
            Character(const.整列先頭[0], const.整列先頭[1], "しょこ"),
            Character(const.整列先頭[0] + const.キャラサイズ, const.整列先頭[1],"さなつん"),
            Character(const.整列先頭[0] + const.キャラサイズ*2, const.整列先頭[1],"はなちゃん"),
            Character(const.整列先頭[0] + const.キャラサイズ*3, const.整列先頭[1],"とくべちゅきあら"),
            Character(const.整列先頭[0] + const.キャラサイズ*4, const.整列先頭[1],"まいか"),
            Character(const.整列先頭[0] + const.キャラサイズ*5, const.整列先頭[1],"いおり"),
            Character(const.整列先頭[0] + const.キャラサイズ*6, const.整列先頭[1],"みりにゃ"),
            Character(const.整列先頭[0] + const.キャラサイズ*7, const.整列先頭[1],"ひとみ"),
            Character(const.整列先頭[0] + const.キャラサイズ*8, const.整列先頭[1],"りさ"),
            Character(const.整列先頭[0] + const.キャラサイズ*9, const.整列先頭[1],"あんな"),
            Character(const.整列先頭[0] + const.キャラサイズ*4.5, const.整列先頭[1] + const.キャラサイズ*2,"さっしー", const.向き.北),
        ]

        self.message = Message()
        self.messanger = "さっしー"

    def start(self):
        pass
    
    def update(self):
        if self.messanger == "さっしー":
            self.message.話す(const.M_TYPE.WINDOW,"さっしー",
                            ["きあらがみつかってよかったぁ～",
                            "これで、みんなそろったね！",
                            "じゃあ、きょうのライブがんばろうね！！"])

            if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                self.messanger = "ナレーター"
                self.message.complete = False

        if not self.message.complete and self.messanger == "ナレーター":
            self.message.話す(const.M_TYPE.STORY,None,
                ["10人がそろったイコラブはさいきょう...",
                "そして、ライブは大成功に終わった"]
                )
            
            if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                self.rpg.change_story(const.STORY.GAMECLEAR)

    def draw(self):
        pyxel.bltm(
            0,0,
            0,
            const.TILE * const.CELL * 4, const.TILE * const.CELL * 3,
            const.L_WIDTH,const.L_HEIGHT)
        for member in self.members:
            member.draw()
        self.message.表示()