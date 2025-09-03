import pyxel
from model.message import Message
import const
from datetime import datetime
import random

class Character():
    def __init__(self, global_x=0, global_y=0, 名前=None, 向き=const.向き.南):
        self.local_x = global_x % const.FIELD
        self.local_y = global_y % const.FIELD
        self.global_x = global_x
        self.global_y = global_y
        self.名前 = 名前
        self.向き = 向き
        self.状態 = const.状態.歩く
        self.舞香ちゃん情報 = {}
        self.message = Message()
        random.seed(datetime.now().timestamp())

    def 状態変更(self, 状態):
        self.状態 = 状態

    def update(self):
        if self.名前 == "さっしー":
             match self.状態:
                case const.状態.立ち止まる:
                    self.立ち止まる()
                case const.状態.話す:
                    self.話す()
        else:
            match self.状態:
                case const.状態.歩く:
                    self.auto_move()
                case const.状態.立ち止まる:
                    self.立ち止まる()
                case const.状態.話す:
                    self.話す()

    def 前に進めるかな(self, x, y):
        return pyxel.tilemaps[0].pget(x //const.CELL ,y //const.CELL) in const.歩けるタイル

    def auto_move(self):
        if pyxel.frame_count % 30 == 0:
            self.向き = random.choice([const.向き.北, const.向き.南, const.向き.西, const.向き.東])

            match self.向き:
                case const.向き.北:
                    if self.前に進めるかな(self.global_x, self.global_y - const.キャラ歩幅):
                        self.local_y -= const.キャラ歩幅
                        self.global_y -= const.キャラ歩幅
                case const.向き.南:
                    if self.前に進めるかな(self.global_x, self.global_y + const.キャラ歩幅):
                        self.local_y += const.キャラ歩幅
                        self.global_y += const.キャラ歩幅
                case const.向き.西:
                    if self.前に進めるかな(self.global_x - const.キャラ歩幅, self.global_y):
                        self.local_x -= const.キャラ歩幅
                        self.global_x -= const.キャラ歩幅
                case const.向き.東:
                    if self.前に進めるかな(self.global_x + const.キャラ歩幅, self.global_y):
                        self.local_x += const.キャラ歩幅
                        self.global_x += const.キャラ歩幅

    def draw(self):
        if self.名前 == "さっしー":
            self.立ち止まる()
            if self.状態 == const.状態.話す:
                self.message.表示()
        else:
            self.歩く()
            if self.状態 == const.状態.話す:
                self.message.表示()
                self.立ち止まる()

    def 歩く(self):
        # if self.状態 == const.状態.歩く:
            # 右足左足の描画切り替え
            #右
            if 0 < pyxel.frame_count % 10 and  pyxel.frame_count % 10 < 5:
                pyxel.blt(self.local_x,self.local_y,0,
                        const.キャラ[self.名前]['右'][self.向き][0],
                        const.キャラ[self.名前]['右'][self.向き][1],
                        const.キャラサイズ,const.キャラサイズ, const.キャラ透過色)
            #左
            else:
                pyxel.blt(self.local_x,self.local_y,0,
                        const.キャラ[self.名前]['左'][self.向き][0],
                        const.キャラ[self.名前]['左'][self.向き][1]
                        ,const.キャラサイズ,const.キャラサイズ,const.キャラ透過色)
                
    def 立ち止まる(self):
        # if self.状態 == const.状態.立ち止まる:
            pyxel.blt(self.local_x,self.local_y,0,
                    const.キャラ[self.名前]['右'][self.向き][0],
                    const.キャラ[self.名前]['右'][self.向き][1],
                    const.キャラサイズ,const.キャラサイズ,const.キャラ透過色)
                
    def 話す(self):
        match self.名前:
            case "はなちゃん":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["あ、まいかちゃん！","ねえねえ、ケータリングの奥に衣装部屋があるの知ってる？"])
            case "みりにゃ":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["ラーメンがないよぉ"])
            case "しょこ":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["きあら、サイリウム買いに行くって言ってたんだよね"])
            case "あんな":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["きあら、メガホンの調整するって外に出たんだよ", "止めれば良かったな..."])
            case "さなつん":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["あ！まいか！", "祝花みた！？","くろしまくんいたんだよ！！"])
            case "ひとみ":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["ねえねえ、まいか！", "ここの会場ってさ", "ステージのうらに隠し部屋があるらしいよ","いってみない？"])
            case "いおり":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["前にきあら", "起きるためには、ひかり・おと・かおり、の３つが大事", "っていってたな..."])
            case "りさ":
                if self.舞香ちゃん情報[const.舞香ちゃん情報キー.会話済メンバー数] >= 4:
                    self.message.話す(const.M_TYPE.WINDOW, self.名前,["この世界ってゴミめいてるよね？","んふっ（笑）"])
                else:
                    self.message.話す(const.M_TYPE.WINDOW, self.名前,["ようすがおかしい！","ようすがおかしい！"])                    
            case "さっしー":
                if self.舞香ちゃん情報[const.舞香ちゃん情報キー.会話済メンバー数] == 8:
                    self.message.話す(const.M_TYPE.WINDOW, self.名前,["さすがまいか","みんなから話を聞いたみたいだね！"])
                else:
                    self.message.話す(const.M_TYPE.WINDOW, self.名前,["めんばーに話を聞くの大事だからね！", "かならず見つけ出して！"])
            case "いなちゃん":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["きあらちゃんのために", "ええイチゴをこうてきたで", "楽屋になかった？"])
            case "ゆずにい":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["きあらちゃん？", "さっき眠そうな顔して", "どこかいきよったで"])
            case "しのぶさん":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["きあらちゃん最初の衣装まちがえてるわ", "こまったわねぇ...", "はやく着替えないといけないのに"])
            case "はせがわさん":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["さしはらによばれてライブみにきたよ", "すげーたのしみ！"])
            case "じろうさん":
                self.message.話す(const.M_TYPE.WINDOW, self.名前,["らっしゃいらっしゃい", "たから釣ってってよ！"])
                
        if self.message.complete and (pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or self.message.complete and pyxel.btnp(pyxel.KEY_RETURN)):
            self.状態変更(const.状態.歩く)
            self.message.complete = False

    def 部屋の場所(self):
        return (self.global_x // const.L_WIDTH, self.global_y // const.L_HEIGHT)
    
    def 舞香ちゃんの情報を得る(self, 舞香ちゃん情報キー, 舞香ちゃん情報):
        self.舞香ちゃん情報[舞香ちゃん情報キー] = 舞香ちゃん情報