import pyxel
from model.message import Message
import const
from model.character import Character
from model.music import Music
from model.item import Item

# 現状MainCharacterは舞香ちゃんを指す、将来的には推しメンバーを選べるようにしたい
class MainCharacter(Character):
    def __init__(self, global_x=0, global_y=0, 名前=None):
        super().__init__(global_x, global_y, 名前)
        self.message = Message()
        self.show_action = False
        self.members = None
        self.会話済メンバー = []
        self.マップ切り替えタイマー = 15
        self.music = Music()
        self.item = Item()
        self.気持ち = None
        self.m_font = pyxel.Font('assets/misaki_gothic_2nd.bdf')
        self.場所 = "楽屋"

        self.動作 = {
             const.状態.立ち止まる: (lambda: print("立ち止まる"), lambda: self.立ち止まる()),
             const.状態.歩く: (lambda: self.操作する(), lambda: self.歩く()),
             const.状態.マップ切り替え: (lambda: self.マップ切り替え(), lambda: self.マップアイキャッチ()),
             const.状態.思う: (lambda: self.気持ちを語る(), lambda: self.気持ちを表示する()),
        }

    def update(self, members):
        self.members = members
        self.動作[self.状態][const.動作_状態_処理]()

    def draw(self):
        self.動作[self.状態][const.動作_状態_描画]()
        self.message.表示()

    def 前に進めるかな(self, x1, y1, x2, y2):
        return pyxel.tilemaps[0].pget(x1 //const.CELL ,y1 //const.CELL) in const.歩けるタイル and pyxel.tilemaps[0].pget(x2 //const.CELL ,y2 //const.CELL) in const.歩けるタイル

    def 気持ちを語る(self):
        # 場所によってセリフを変える
        self.message.話す(const.M_TYPE.WINDOW, self.名前, self.気持ち)

    def 気持ちを表示する(self):
         self.立ち止まる()
         self.message.表示()

    def 操作する(self):
        # print(self.local_x, self.local_y, self.global_x, self.global_y, self.向き)
        #
        #  (x,y)-------(x+16,y)
        #    |             |
        #    |   キャラ    |
        #    |             |
        #  (x,y+16)---(x+16,y+16)
        #
        self.local_x = self.global_x % const.FIELD
        self.local_y = self.global_y % const.FIELD

        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT,const.HOLD,const.REPEAT) or pyxel.btnp(pyxel.KEY_LEFT,const.HOLD,const.REPEAT):
                self.向き = const.向き.西
                if self.前に進めるかな(self.global_x+4 - const.当たり判定マージン, self.global_y, self.global_x+4 - const.当たり判定マージン, self.global_y + const.キャラサイズ-1) and not self.メンバーとの接触チェック(self.local_x - const.当たり判定マージン, self.local_y):
                    self.global_x -= const.キャラ歩幅

                    self.足元チェック(self.global_x, self.global_y)

                    if self.local_x <= 0 and self.global_x >= 0:
                        self.状態 = const.状態.マップ切り替え
                        self.local_x = const.FIELD - const.キャラサイズ
                        self.global_x -= const.キャラサイズ
        elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT,const.HOLD,const.REPEAT) or pyxel.btnp(pyxel.KEY_RIGHT,const.HOLD,const.REPEAT):
                self.向き = const.向き.東
                if self.前に進めるかな(self.global_x + const.キャラサイズ-6 + const.当たり判定マージン, self.global_y, self.global_x + const.キャラサイズ-6 + const.当たり判定マージン, self.global_y + const.キャラサイズ-1) and not self.メンバーとの接触チェック(self.local_x + const.当たり判定マージン, self.local_y):
                    self.global_x += const.キャラ歩幅

                    self.足元チェック(self.global_x, self.global_y)

                    if (self.local_x + const.キャラサイズ) / const.FIELD >= 1:
                        self.状態 = const.状態.マップ切り替え
                        self.local_x = 0
                        self.global_x += const.キャラサイズ
        elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP,const.HOLD,const.REPEAT) or pyxel.btnp(pyxel.KEY_UP,const.HOLD,const.REPEAT):
                self.向き = const.向き.北
                if self.前に進めるかな(self.global_x+5, self.global_y - const.当たり判定マージン, self.global_x + const.キャラサイズ-5, self.global_y - const.当たり判定マージン) and not self.メンバーとの接触チェック(self.local_x, self.local_y - const.当たり判定マージン):
                    self.global_y -= const.キャラ歩幅

                    self.足元チェック(self.global_x, self.global_y)

                    if self.local_y <= 0 and self.global_y >= 0:
                        self.状態 = const.状態.マップ切り替え
                        self.local_y = const.FIELD - const.キャラサイズ
                        self.global_y -= const.キャラサイズ
        elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN,const.HOLD,const.REPEAT) or pyxel.btnp(pyxel.KEY_DOWN,const.HOLD,const.REPEAT):
                self.向き = const.向き.南
                if self.前に進めるかな(self.global_x+5, self.global_y + const.キャラサイズ + const.当たり判定マージン, self.global_x + const.キャラサイズ-5 , self.global_y + const.キャラサイズ + const.当たり判定マージン) and not self.メンバーとの接触チェック(self.local_x, self.local_y + const.当たり判定マージン ):
                    self.global_y += const.キャラ歩幅

                    self.足元チェック(self.global_x, self.global_y)

                    if (self.local_y + const.キャラサイズ) / const.FIELD >= 1:
                        self.状態 = const.状態.マップ切り替え
                        self.local_y = 0
                        self.global_y += const.キャラサイズ
                        
    def メンバーとの接触チェック(self, x, y):
        if self.状態 == const.状態.歩く:
            for member in self.members:
                if x < member.local_x + const.キャラサイズ and x + const.キャラサイズ > member.local_x and y < member.local_y + const.キャラサイズ and y + const.キャラサイズ > member.local_y and member.部屋の場所() == self.部屋の場所():
                        # 接触した場合の処理 
                        member.状態変更(const.状態.話す)
                        if member.名前 not in self.会話済メンバー and member.名前 != "さっしー" and member.名前 != "しのぶさん" and member.名前 != "ゆずにい" and member.名前 != "いなちゃん" and member.名前 != "はせがわさん" and member.名前 != "じろうさん":
                            self.会話済メンバー.append(member.名前)
                        return True
        return False

    def 足元チェック(self, x, y):
        x = x + const.キャラサイズ // 2
        y = y + const.キャラサイズ // 2
        if pyxel.tilemaps[0].pget(x //const.CELL ,y //const.CELL) in const.階段_ケータリング:
             pyxel.play(const.BGMチャンネル, [const.階段音])
             self.global_x = const.階段脇_衣装部屋[const.階段_X座標Idx]
             self.global_y = const.階段脇_衣装部屋[const.階段_Y座標Idx]
        elif pyxel.tilemaps[0].pget(x //const.CELL ,y //const.CELL) in const.階段_衣装部屋:
            pyxel.play(const.BGMチャンネル, [const.階段音])
            self.global_x = const.階段脇_ケータリング[const.階段_X座標Idx]
            self.global_y = const.階段脇_ケータリング[const.階段_Y座標Idx]
        elif pyxel.tilemaps[0].pget(x //const.CELL ,y //const.CELL) in const.階段_ステージ裏:
            pyxel.play(const.BGMチャンネル, [const.階段音])
            self.global_x = 46*const.CELL#const.階段脇_隠し部屋[const.階段_X座標Idx] 
            self.global_y = 140*const.CELL#const.階段脇_隠し部屋[const.階段_Y座標Idx]
        elif pyxel.tilemaps[0].pget(x //const.CELL ,y //const.CELL) in const.階段_隠し部屋:
            pyxel.play(const.BGMチャンネル, [const.階段音])
            self.global_x = const.階段脇_ステージ裏[const.階段_X座標Idx]
            self.global_y = const.階段脇_ステージ裏[const.階段_Y座標Idx]
        elif pyxel.tilemaps[0].pget(x //const.CELL ,y //const.CELL) in const.アイテム_拡声器_識別:
            pyxel.play(const.BGMチャンネル, [const.アイテム取得])
            pyxel.tilemaps[0].pset(const.アイテム_拡声器_配置[0][0],const.アイテム_拡声器_配置[0][1],const.タイル_拡声器とったあと[0])
            pyxel.tilemaps[0].pset(const.アイテム_拡声器_配置[1][0],const.アイテム_拡声器_配置[1][1],const.タイル_拡声器とったあと[1])
            pyxel.tilemaps[0].pset(const.アイテム_拡声器_配置[2][0],const.アイテム_拡声器_配置[2][1],const.タイル_拡声器とったあと[2])
            pyxel.tilemaps[0].pset(const.アイテム_拡声器_配置[3][0],const.アイテム_拡声器_配置[3][1],const.タイル_拡声器とったあと[3])
            self.item.アイテムを追加(const.アイテム.めがほん.value)
        elif pyxel.tilemaps[0].pget(x //const.CELL ,y //const.CELL) in const.アイテム_とちぎのいちご_識別:
            pyxel.play(const.BGMチャンネル, [const.アイテム取得])
            pyxel.tilemaps[0].pset(const.アイテム_とちぎのいちご_配置[0][0],const.アイテム_とちぎのいちご_配置[0][1],const.タイル_とちぎのいちごとったあと[0])
            pyxel.tilemaps[0].pset(const.アイテム_とちぎのいちご_配置[1][0],const.アイテム_とちぎのいちご_配置[1][1],const.タイル_とちぎのいちごとったあと[1])
            pyxel.tilemaps[0].pset(const.アイテム_とちぎのいちご_配置[2][0],const.アイテム_とちぎのいちご_配置[2][1],const.タイル_とちぎのいちごとったあと[2])
            pyxel.tilemaps[0].pset(const.アイテム_とちぎのいちご_配置[3][0],const.アイテム_とちぎのいちご_配置[3][1],const.タイル_とちぎのいちごとったあと[3])
            self.item.アイテムを追加(const.アイテム.とちぎのいちご.value)
        elif pyxel.tilemaps[0].pget(x //const.CELL ,y //const.CELL) in const.アイテム_サイリウム_識別:
            pyxel.play(const.BGMチャンネル, [const.アイテム取得])
            pyxel.tilemaps[0].pset(const.アイテム_サイリウム_配置[0][0],const.アイテム_サイリウム_配置[0][1],const.タイル_サイリウムとったあと[0])
            pyxel.tilemaps[0].pset(const.アイテム_サイリウム_配置[1][0],const.アイテム_サイリウム_配置[1][1],const.タイル_サイリウムとったあと[1])
            pyxel.tilemaps[0].pset(const.アイテム_サイリウム_配置[2][0],const.アイテム_サイリウム_配置[2][1],const.タイル_サイリウムとったあと[2])
            pyxel.tilemaps[0].pset(const.アイテム_サイリウム_配置[3][0],const.アイテム_サイリウム_配置[3][1],const.タイル_サイリウムとったあと[3])
            self.item.アイテムを追加(const.アイテム.さいりうむ.value)

        self.local_x = self.global_x % const.FIELD
        self.local_y = self.global_y % const.FIELD
        self.状態 = const.状態.歩く

    def マップ切り替え(self):
        if self.状態 == const.状態.マップ切り替え:
            self.マップ切り替えタイマー -= 1
            self.music.BGMランダム再生()
            self.場所判定(self.global_x,self.global_y)
            if self.マップ切り替えタイマー == 0:
                self.状態 = const.状態.歩く
                self.マップ切り替えタイマー = 15

    def マップアイキャッチ(self):
        pyxel.cls(const.色.RED.value)
        pyxel.text((const.L_WIDTH - len(const.TITLE) * const.FONT_SIZE )/2, const.L_HEIGHT/2, const.TITLE, const.色.PINK.value, self.m_font)

    def 場所判定(self,x,y):
        # マップの場所を判定して、部屋の場所を返す
        for 部屋の種類 in const.部屋:
            部屋の座標 = const.部屋[部屋の種類]
            if (部屋の座標[0][0] <= x <= 部屋の座標[0][1] and 部屋の座標[1][0] <= y <= 部屋の座標[1][1]):
                 self.場所 = 部屋の種類
                 break

    def 場所表示(self,x,y):
            pyxel.rect(const.R_POS_x,const.R_POS_y,const.R_WIDTH,const.R_HEIGHT, const.色.ORANGE.value)
            pyxel.text(const.R_POS_x + const.FONT_SIZE/2, const.R_POS_y + 2 ,self.場所, const.色.WHITE.value, self.m_font)

    def getMusic(self):
        return self.music
    
    def getItem(self):
        return self.item
    
    def 持ってるアイテム(self):
         return self.item.アイテム