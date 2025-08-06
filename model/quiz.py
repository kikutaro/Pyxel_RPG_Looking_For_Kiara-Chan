import pyxel
import const
import random
from model.menu import Menu

class Quiz:
    def __init__(self, rpg):
        self.rpg = rpg
        self.状態 = "問題"
        self.問題数 = 5
        self.正解数 = 0
        self.回答数 = 0
        self.選択 = 0
        self.問題 = [
            #きあらちゃん
            {
                "問題": "きあらちゃんセンターの表題曲は？",
                "選択肢": ["トップノートしか知らない", "ミドルノートしか知らない", "ラストノートしかしらない"],
                "正解": 2
            },
            {
                "問題": "きあらちゃんの出身地は？",
                "選択肢": ["栃木県", "群馬県", "茨城県"],
                "正解": 0
            },
            {
                "問題": "きあらちゃんの必殺技は？",
                "選択肢": ["どくしゅ", "でゅくし", "でゅぐじ"],
                "正解": 1
            },
            {
                "問題": "きあらちゃんがSNSをはじめたときのハプニングは？",
                "選択肢": ["Twitterアカウントが凍結された", "Twitterアカウントが乗っ取られた", "Twitterアカウントにログインできなくなった"],
                "正解": 0
            },
            #はなちゃん
            {
                "問題": "はなちゃんのファンの呼称は？",
                "選択肢": ["はなちゃんず", "はなまる", "ふらわー"],
                "正解": 1
            },
            {
                "問題": "はなちゃんの個人ブログ名は？",
                "選択肢": ["はなまるきぶん", "はなまるうどん", "はなまるきくん"],
                "正解": 0
            },
            {
                "問題": "はなちゃんが連載している漫画は？",
                "選択肢": ["はな漫", "はなカートゥーン", "はなコミ！"],
                "正解": 2
            },
            #まいかちゃん
            {
                "問題": "まいかちゃんが出演したドラマ「キャスター」の役名は？",
                "選択肢": ["戸山紗矢", "戸川紗矢", "戸海紗矢"],
                "正解": 0
            },
            #いおりちゃん
            {
                "問題": "いおりちゃんのファースト写真集のタイトルは？",
                "選択肢": ["君に教えたいこと", "君だけに教えてあげる", "君にしか教えない"],
                "正解": 2
            },
            #さなつん
            {
                "問題": "さなつんのソロコンサートで初披露された曲は？",
                "選択肢": ["宝物はグリーン", "My Voice Is For You", "僕のヒロイン"],
                "正解": 0
            },
            #あんなちゃん
            {
                "問題": "あんなちゃんが振り付けした楽曲は？",
                "選択肢": ["拝啓、貴方様", "真夜中マーメイド", "Kiara Tiara"],
                "正解": 1
            },
            #ひとみちゃん
            {
                "問題": "ひとみちゃんが表紙のじゆうちょうに書かれた文字は？",
                "選択肢": ["ぎゃああああ！", "どひゃあああ！", "ひやああああ！"],
                "正解": 2
            },
            #りさちー
            {
                "問題": "りさちゃんセンターの楽曲は？",
                "選択肢": ["お姉様にしてよ！", "お姫様にしてよ!", "お嬢様にしてよ！"],
                "正解": 1
            },
            #しょうこちゃん
            {
                "問題": "しょこちゃんがサブ4を達成したフルマラソンのタイムは？",
                "選択肢": ["3時間57分07秒", "3時間58分08秒", "3時間59分09秒"],
                "正解": 0
            },
            #みりにゃ
            {
                "問題": "みりにゃプロデュースのブランドは？",
                "選択肢": ["ロスミューズ", "ロゼミューズ", "ロゼミューゼ"],
                "正解": 1
            },
            #さしはらさん
            {
                "問題": "さしはらさんの愛称に該当しないものは？",
                "選択肢": ["さっしー", "さしこ", "SASUKE"],
                "正解": 2
            }
        ]
        self.問題番号 = random.randint(0, len(self.問題) - 1)
        self.メニュー = Menu(None, const.色.WHITE.value, const.色.RED.value, [
            ("もういちど挑戦する", lambda: self.__init__(rpg)),
            ("タイトルに戻る", lambda: self.タイトルに戻る()),
            ("ゲームを終了する", lambda: self.ゲームを終了する())
        ])

    def タイトルに戻る(self):
        self.rpg.change_story(const.STORY.TITLE)

    def ゲームを終了する(self):
        pyxel.quit()

    def 回答する(self):
        match self.状態:
            case "問題":
                if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btnp(pyxel.KEY_UP):
                        pyxel.play(const.BGMチャンネル, [const.メニュー音])
                        self.選択 -= 1
                        if self.選択 < 0:
                            self.選択 = len(self.問題[0]["選択肢"]) - 1
                if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btnp(pyxel.KEY_DOWN):
                        pyxel.play(const.BGMチャンネル, [const.メニュー音])
                        self.選択 += 1
                        if self.選択 >= len(self.問題[0]["選択肢"]):
                            self.選択 = 0

                if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.KEY_RETURN):
                    if self.選択 == self.問題[self.問題番号]["正解"]:
                        self.正解数 += 1
                        self.アタリ()
                        pyxel.play(const.BGMチャンネル, [const.アタリ音])
                    else:
                        self.ハズレ()
                        pyxel.play(const.BGMチャンネル, [const.ハズレ音])

                    self.回答数 += 1
                    self.状態 = "回答"                    
                
            case "回答":
                if self.問題数 == self.回答数:
                    self.状態 = "終了"
                else:
                    self.状態 = "問題"
                    self.問題.remove(self.問題[self.問題番号])
                    self.問題番号 = random.randint(0, len(self.問題) - 1)

            case "終了":
                self.メニュー.update()
            
    def draw(self):
        match self.状態:
            case "問題":
                pyxel.cls(const.色.PINK.value)
                pyxel.rect(const.Q_POS_X, const.Q_POS_Y, const.Q_WIDTH, const.Q_HEIGHT, const.色.WHITE.value)
                pyxel.text(const.Q_POS_X + const.Q_PADDING, const.Q_POS_Y + const.Q_PADDING, self.問題[self.問題番号]["問題"], const.色.BLACK.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                pyxel.rect(const.A_POS_X, const.A_POS_Y, const.A_WIDTH, const.A_HEIGHT, const.色.WHITE.value)
                pyxel.text(const.Q_POS_X + const.A_WIDTH - len("正解数 0/0") * const.FONT_SIZE , const.Q_HEIGHT+const.A_HEIGHT, "正解数 " + str(self.正解数) +"/" + str(self.回答数), const.色.BLUE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                for i, choice in enumerate(self.問題[self.問題番号]["選択肢"]):
                    pyxel.text(const.A_POS_X + const.A_PADDING, const.A_POS_Y + const.A_PADDING + i * 10, f"{i + 1}. {choice}", const.色.RED.value if self.選択 == i else const.色.BLACK.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
            case "終了":
                pyxel.cls(const.色.BLACK.value)
                pyxel.text(const.Q_POS_X , const.Q_HEIGHT, "正解数 " + str(self.正解数) +"/" + str(self.回答数), const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                match self.正解数:
                    case 0:
                        評価 = "残念！"
                    case 1 | 2:
                        評価 = "頑張ったね！"
                    case 3 | 4:
                        評価 = "すごい！"
                    case _:
                        評価 = "キミはイコラブクイズ王だね！"
                pyxel.text(const.Q_POS_X , const.Q_HEIGHT + const.FONT_SIZE, 評価, const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                self.メニュー.draw()

    def アタリ(self):
        pyxel.circb(const.FIELD / 2 , const.FIELD / 2 ,50, const.色.RED.value)
        pyxel.circb(const.FIELD / 2 , const.FIELD / 2 ,48, const.色.RED.value)

    def ハズレ(self):
        pyxel.line(const.FIELD / 2 - 50, const.FIELD / 2 - 50, const.FIELD / 2 + 50, const.FIELD / 2 + 50, const.色.RED.value)
        pyxel.line(const.FIELD / 2 + 50, const.FIELD / 2 - 50, const.FIELD / 2 - 50, const.FIELD / 2 + 50, const.色.RED.value)
        
        