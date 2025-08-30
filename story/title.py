import pyxel
import const
from model.menu import Menu
from model.character import Character

class Title:
    def __init__(self, rpg):
        self.rpg = rpg
        #モード
        self.mode = const.OPENING_MODE.OPENING

        #タイトルの縦座標（上から下に移動する）
        self.title_y = 0
        #タイトルのセンターX座標
        self.text_center = (int(const.L_WIDTH) - (len(const.TITLE) * int(const.TITLE_FONT_SIZE)))/2

        self.members = [
            Character(const.TILE*3 , const.TILE*3,"しょこ"),
            Character(const.TILE*4 , const.TILE*3,"さなつん"),
            Character(const.TILE*5, const.TILE*3,"はなちゃん"),
            Character(const.TILE*6, const.TILE*3,"きあら"),
            Character(const.TILE*7, const.TILE*3,"まいか"),
            Character(const.TILE*8, const.TILE*3,"いおり"),
            Character(const.TILE*9, const.TILE*3,"みりにゃ"),
            Character(const.TILE*10, const.TILE*3,"ひとみ"),
            Character(const.TILE*11, const.TILE*3,"りさ"),
            Character(const.TILE*12, const.TILE*3,"あんな")
        ]

        self.menu = Menu(
            const.色.PINK.value,
            const.色.WHITE.value,
            const.色.RED.value,
            [
            ("おーぷにんぐから", lambda: self.rpg.change_story(const.STORY.OPENING)),
            ("ゲームから", lambda: self.rpg.change_story(const.STORY.PLAY)),
            ("めんばーずかん", lambda: self.rpg.change_story(const.STORY.BOOK)),
            ("くいず", lambda: self.rpg.change_story(const.STORY.QUIZ)),
            ("みゅーじっくぼっくす", lambda: self.rpg.change_story(const.STORY.BGM))
            # ("おわり", lambda: self.rpg.change_story(const.STORY.GAMECLEAR))
            ])
        
        self.音楽再生回数 = 0
    
    def start(self):
        if self.音楽再生回数 == 0:
            self.音楽再生回数 += 1
            pyxel.playm(0)

    def update(self):
        if self.mode == const.OPENING_MODE.OPENING:
            self.title_y += 1

            for member in self.members:
                member.local_y += 1
                if member.local_y > const.L_HEIGHT / 2:
                    member.local_y = const.L_HEIGHT / 2
            
            #リターンかスタートが押されたら音楽を止めてオープニングに遷移
            if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.KEY_RETURN):
                self.mode = const.OPENING_MODE.MENU
                pyxel.stop()
                self.メニュー表示()
        elif self.mode == const.OPENING_MODE.MENU:
            self.menu.update()

    def draw(self):
        if self.mode == const.OPENING_MODE.OPENING:
            pyxel.cls(const.色.PINK.value)
            self.paint_graduation()
            for member in self.members:
                member.draw()
            
            self.オープニング表示()
        elif self.mode == const.OPENING_MODE.MENU:
            pyxel.cls(const.色.PINK.value)
            self.メニュー表示()

    def paint_graduation(self):
        self.paint_row_graduation(4, 8)
        self.paint_col_graduation(4, 8)

    def paint_row_graduation(self, num_grads, grad_length):
        for i in range(num_grads, 1, -1):
            pyxel.dither(i / num_grads)
            pyxel.rect(
                0,
                (num_grads - i) * grad_length,
                pyxel.width,
                grad_length,
                const.色.RED.value
                )
            pyxel.rect(
                0,
                pyxel.height - grad_length - (num_grads - i) * grad_length,
                pyxel.width,
                grad_length,
                const.色.RED.value
                )
        
        pyxel.dither(1)

    def paint_col_graduation(self, num_grads, grad_length):
        for i in range(num_grads, 1, -1):
            pyxel.dither(i / num_grads)
            pyxel.rect(
                (num_grads - i) * grad_length,
                0,
                grad_length,
                pyxel.height,
                const.色.RED.value
                )
            pyxel.rect(
                pyxel.width - grad_length - (num_grads - i) * grad_length,
                0,
                grad_length,
                pyxel.height,                
                const.色.RED.value
                )
        
        pyxel.dither(1)

    def オープニング表示(self):
        if self.title_y < const.GAME_TITLE_POS_Y:
            pyxel.text(self.text_center, 20 + self.title_y , const.TITLE, 7, self.rpg.t_font)
            pyxel.text(self.text_center + 1, 20 + self.title_y + 1 , const.TITLE, 2, self.rpg.t_font)
        else:
            pyxel.text(self.text_center, 20 + const.GAME_TITLE_POS_Y , const.TITLE, 7, self.rpg.t_font)
            pyxel.text(self.text_center + 1, 20 + const.GAME_TITLE_POS_Y, const.TITLE, 2, self.rpg.t_font)
            pyxel.text(self.text_center, 35 + const.GAME_TITLE_POS_Y , const.M_GAME_START, pyxel.frame_count % 16,self.rpg.m_font)


    def メニュー表示(self):
        self.menu.draw()