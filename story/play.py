import pyxel
import const
from model.main_character import MainCharacter
from model.character import Character
from model.message import Message
from model.timer import Timer
from model.item import Item
import random

class Play:
    def __init__(self, rpg):
        self.rpg = rpg
        self.room = [0,0]
        self.timer = Timer()
        self.item = Item()
        self.message = Message()
        self.舞香ちゃん = MainCharacter(
            const.舞香ちゃんが最初にいる場所[0],
            const.舞香ちゃんが最初にいる場所[1],"まいか")
        self.舞香ちゃん.message = self.message
        
        self.members = [
            Character(const.TILE*12,const.TILE*6,"はなちゃん"),
            Character(const.TILE*21,const.TILE*23,"みりにゃ"),
            Character(const.TILE*40,const.TILE*10,"しょこ"),
            Character(const.TILE*51,const.TILE*6,"あんな"),
            Character(const.TILE*38,const.TILE*41,"さなつん"),
            Character(const.TILE*22,const.TILE*38,"ひとみ"),
            Character(const.TILE*9,const.TILE*58,"いおり"),
            Character(const.TILE*61,const.TILE*57,"りさ"),
            Character(const.TILE*32,const.TILE*30,"さっしー", const.向き.東),
            Character(const.TILE*40,const.TILE*56,"いなちゃん"),
            Character(const.TILE*60,const.TILE*42,"ゆずにい"),
            Character(const.TILE*10,const.TILE*70,"しのぶさん"),
            Character(const.TILE*56,const.TILE*29,"はせがわさん"),
            Character(const.TILE*25,const.TILE*54,"じろうさん"),
        ]

        self.くろしまトーク = False
        self.きあらちゃんおっき = False
        self.クリア = False

        self.情報表示 = True

        self.くろしまランダムセリフ = [
            ["Here we are!うちらの...","LEADER!"],
            ["なんでもチャレンジ...","ACTIVE Girl!"],
            ["かわいい 魅惑の...","MERMAID!"],
            ["甘美なAngel","デビルの誘惑!"],
            ["Princess...","の国から飛んできたとよ!"],
            ["ハイトーン飾る あふれる...","Smile!"],
            ["君の好きな声でいたいな...","DIVA！"],
            ["みりにゃ 女子の憧れ...","Sweetie Girl!"],
            ["みんなを照らすよ！","SUNNY！"],
            ["努力型 天才...","Performer!"]
        ]

        self.くろしま今回のセリフ = random.choice(self.くろしまランダムセリフ)

        self.くろしまセリフ = ["さなちゃんとはなしたようだね","さなきあにはおせわになってるから魔法をかけてあげよう" ,"さあ、あるいてみて！"]
        self.くろしまセリフ[2:2] = self.くろしま今回のセリフ

    def start(self):
        pyxel.stop()
        self.舞香ちゃん.getMusic().BGMランダム再生()
        self.舞香ちゃん.getMusic().BGM名表示()
        self.message.messanger = "まいか"
        self.timer.カウントスタート()

    def update(self):
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X) or pyxel.btnp(pyxel.KEY_A):
            self.情報表示 = not self.情報表示

        if ("さなつん" in self.舞香ちゃん.会話済メンバー and self.舞香ちゃん.global_x // const.CELL, self.舞香ちゃん.global_y // const.CELL) in const.くろしままえ and not self.くろしまトーク and self.舞香ちゃん.向き == const.向き.北:
            self.message.話す(const.M_TYPE.WINDOW, 
                            "くろしまくん", self.くろしまセリフ)
            const.キャラ歩幅 = 8

            if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                self.message.complete = False
                self.message.messages.clear()
                self.くろしまトーク = True
                self.message.messanger = "まいか"

        if self.舞香ちゃん.部屋の場所() == const.最後の部屋:
            if self.message.messanger == "まいか" and len(self.舞香ちゃん.持ってるアイテム()) == 0 or const.アイテム.さいりうむ.value not in self.舞香ちゃん.持ってるアイテム():
                self.message.話す(const.M_TYPE.WINDOW,
                            "まいか",
                            ["うわっ、なにここ！？","暗くて何も見えない...戻ろう"])
                    
                if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                    self.舞香ちゃん.global_x = const.階段脇_ステージ裏[const.階段_X座標Idx]
                    self.舞香ちゃん.global_y = const.階段脇_ステージ裏[const.階段_Y座標Idx]
                    self.message.complete = False
                    self.message.messages.clear()
            else:
                if self.message.messanger == "まいか" and self.message.cnt == 0:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "まいか",
                                    ["さいりうむの明かりで見える！","あ！きあらちゃん！！！", "こんなところにいたの！？", "え、寝てる！？"])

                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.message.messanger = "まいか"
                            self.message.complete = False
                            self.message.cnt += 1

                if(not const.アイテム.めがほん.value in self.舞香ちゃん.持ってるアイテム() and not const.アイテム.とちぎのいちご.value in self.舞香ちゃん.持ってるアイテム()):
                    if self.message.messanger == "まいか" and self.message.cnt == 1:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "まいか",
                                    ["ゆさゆさ", "おきて、きあら！", "だめだ、ぜんぜん起きない..."])


                if(const.アイテム.めがほん.value in self.舞香ちゃん.持ってるアイテム() and not const.アイテム.とちぎのいちご.value in self.舞香ちゃん.持ってるアイテム()):
                    if self.message.messanger == "まいか" and self.message.cnt == 1:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "まいか",
                                    ["そうだ、メガホン！", "あーあー", "きあらちゃん、起きてー！"])
                        
                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.message.messanger = "きあら"
                            self.message.complete = False
                            self.message.cnt += 1

                    if self.message.messanger == "きあら" and self.message.cnt == 2:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "きあら",
                                    ["zzzzz..."])
                            
                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.message.messanger = "まいか"
                            self.message.complete = False
                            self.message.cnt += 1

                    if self.message.messanger == "まいか" and self.message.cnt == 3:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "まいか",
                                    ["音だけじゃダメか..."])
                        
                if(not const.アイテム.めがほん.value in self.舞香ちゃん.持ってるアイテム() and const.アイテム.とちぎのいちご.value in self.舞香ちゃん.持ってるアイテム()):
                    if self.message.messanger == "まいか" and self.message.cnt == 1:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "まいか",
                                    ["そうだ、いちご！", "きあらちゃん、とちぎのいちごだよー！","いい香りだよー、起きてー！"])
                        
                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.message.messanger = "きあら"
                            self.message.complete = False
                            self.message.cnt += 1

                    if self.message.messanger == "きあら" and self.message.cnt == 2:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "きあら",
                                    ["zzzzz..."])
                            
                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.message.messanger = "まいか"
                            self.message.complete = False
                            self.message.cnt += 1

                    if self.message.messanger == "まいか" and self.message.cnt == 3:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "まいか",
                                    ["匂いだけじゃダメか..."])
                        
                if(const.アイテム.めがほん.value in self.舞香ちゃん.持ってるアイテム() and const.アイテム.とちぎのいちご.value in self.舞香ちゃん.持ってるアイテム()):
                    if self.message.messanger == "まいか" and self.message.cnt == 1:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "まいか",
                                    ["よし、いちごを鼻に置くよ、いい香り", "そんで、メガホン！", "あーあー", "きあらちゃん、起きてー！"])
                        
                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.message.messanger = "きあら"
                            self.message.complete = False
                            self.message.cnt += 1
                            self.きあらちゃんおっき = True
                        
                    if self.message.messanger == "きあら" and self.message.cnt == 2:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "きあら",
                                    ["zzzzz...ん、まぶしい", "え、舞香ちゃんの声...？","あ？いちごの香り？","あ！舞香ちゃん！！"])
                        
                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.message.messanger = "まいか"
                            self.message.complete = False
                            self.message.cnt += 1

                    if self.message.messanger == "まいか" and self.message.cnt == 3:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "まいか",
                                    ["きあらやっとおきた！", "いそいできがえて！", "みんなまってるよ！"])
                        
                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.message.messanger = "きあら"
                            self.message.complete = False
                            self.message.cnt += 1
                        
                    if self.message.messanger == "きあら" and self.message.cnt == 4:
                        self.message.話す(const.M_TYPE.WINDOW,
                                    "きあら",
                                    ["はいっ！"])
                        
                        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                            self.クリア = True

                        #えんでぃんぐへ

                if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btn(pyxel.KEY_RETURN)):
                    #戻る
                    self.舞香ちゃん.global_x = const.階段脇_ステージ裏[const.階段_X座標Idx]
                    self.舞香ちゃん.global_y = const.階段脇_ステージ裏[const.階段_Y座標Idx]
                    self.message.cnt = 0
                    self.message.messages.clear()
        else:
            self.舞香ちゃん.update(self.members)
            for member in self.members:
                if member.名前 == "さっしー":
                    member.舞香ちゃんの情報を得る(const.舞香ちゃん情報キー.会話済メンバー数, len(self.舞香ちゃん.会話済メンバー))
                member.update()

    def draw(self):
        if not self.クリア:
            # pyxel.text(0,0, str(pyxel.frame_count), 7)
            self.マップ更新(self.舞香ちゃん.global_x, self.舞香ちゃん.global_y)
            # print(self.舞香ちゃん.global_x, self.舞香ちゃん.global_y)
            if self.情報表示:
                self.舞香ちゃん.getMusic().BGM名表示()
                self.舞香ちゃん.getItem().表示()
                self.舞香ちゃん.場所表示(self.舞香ちゃん.global_x, self.舞香ちゃん.global_y)
                self.timer.表示()

            if self.舞香ちゃん.部屋の場所() == const.最後の部屋 and (len(self.舞香ちゃん.持ってるアイテム()) == 0  or const.アイテム.さいりうむ.value not in self.舞香ちゃん.持ってるアイテム()):
                pyxel.cls(const.色.BLACK.value)
            
            for member in self.members:
                if member.部屋の場所() == self.舞香ちゃん.部屋の場所():
                    if member.名前 == "さっしー" and member.舞香ちゃん情報[const.舞香ちゃん情報キー.会話済メンバー数] >= 0:
                        member.global_x = 528
                        member.global_y = 496
                        member.local_x = member.global_x % const.FIELD
                        member.local_y = member.global_y % const.FIELD
                        member.向き = const.向き.東 
                        member.draw()
                    member.draw()
                    # break
            self.舞香ちゃん.draw()
            self.message.表示()

            if(self.きあらちゃんおっき):
                きあら = Character(const.TILE * 40, const.FIELD + const.TILE * 6,"きあら")
                きあら.draw()
                pyxel.tilemaps[0].pset(const.寝てるきあら[0][0], const.寝てるきあら[0][1], const.タイル_きあらが寝てる床[0])
                pyxel.tilemaps[0].pset(const.寝てるきあら[1][0], const.寝てるきあら[1][1], const.タイル_きあらが寝てる床[1])
                pyxel.tilemaps[0].pset(const.寝てるきあら[2][0], const.寝てるきあら[2][1], const.タイル_きあらが寝てる床[2])
                pyxel.tilemaps[0].pset(const.寝てるきあら[3][0], const.寝てるきあら[3][1], const.タイル_きあらが寝てる床[3])
        else:
            #クリア画面
            pyxel.cls(const.色.WHITE.value)
            mes1 = "さがしてくれて、ありがとう！"
            mes2 = "このスクリーンをキャプチャしてタイムをきそってね！"
            mes3 = "クリアタイム"
            pyxel.text(self.X軸センタリング(mes1, const.FONT_SIZE), 60, mes1, const.色.BLACK.value, self.rpg.m_font)
            pyxel.text(self.X軸センタリング(mes2, const.FONT_SIZE), 80, mes2, const.色.BLACK.value, self.rpg.m_font)
            pyxel.text(self.X軸センタリング(mes3, const.FONT_SIZE), 100, mes3 , const.色.BLACK.value, self.rpg.m_font)

            #右
            if 0 < pyxel.frame_count % 10 and  pyxel.frame_count % 10 < 5:
                pyxel.blt((const.FIELD - const.キャラサイズ) / 2, (const.FIELD - const.キャラサイズ) / 2,0,
                    const.キャラ['とくべちゅきあら']['右'][const.向き.南][0],
                    const.キャラ['とくべちゅきあら']['右'][const.向き.南][1],
                    const.キャラサイズ,const.キャラサイズ, const.色.WHITE.value)
            #左
            else:
                pyxel.blt((const.FIELD - const.キャラサイズ) / 2, (const.FIELD - const.キャラサイズ) / 2,0,
                    const.キャラ['とくべちゅきあら']['左'][const.向き.南][0],
                    const.キャラ['とくべちゅきあら']['左'][const.向き.南][1],
                    const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)

            mes4 = str(self.timer.経過時間) + "秒"
            pyxel.text(self.X軸センタリング(mes4, const.TITLE_FONT_SIZE), 145, mes4, const.色.BLACK.value, self.rpg.t_font)

            if pyxel.btn(pyxel.KEY_RETURN):
                pass
        
    def X軸センタリング(self, text, font_size):
        return ((const.FIELD - len(text) * font_size)) / 2

    def マップ更新(self,x座標,y座標):
        pyxel.cls(const.色.WHITE.value)
        描画マップx = (x座標 + const.キャラサイズ // 2) // const.FIELD * const.FIELD
        描画マップy = (y座標 + const.キャラサイズ // 2) // const.FIELD * const.FIELD
        pyxel.bltm(0,0,0, 描画マップx, 描画マップy, const.FIELD,const.FIELD)