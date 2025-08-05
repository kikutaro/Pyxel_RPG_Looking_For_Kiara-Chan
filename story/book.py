import pyxel
import const
from model.menu import Menu
from enum import Enum, auto

class Book:
    def __init__(self, rpg):
        if const.DEBUG:
            print("Book.__init__")

        self.メンバープロフィール = {
            'おおたにえみり': [self.おおたにえみり,{
                'けつえきがた': 'O',
                'せいざ': 'うおざ',
                'しんちょう': '155cm',
                'せいねんがっぴ': '1998-3-15',
                'しゅっしんち': 'とうきょうと',
                'しゅみ': ['メイクやファッションをたのしむこと', 'らーめんめぐり'],
                'とくぎ': ['ジョッキもち'],
            }],
            'おおばはな': [self.おおばはな,{
                'けつえきがた': 'A',
                'せいざ': 'みずがめざ',
                'しんちょう': '160cm',
                'せいねんがっぴ': '2000-2-4',
                'しゅっしんち': 'さいたまけん',
                'しゅみ': ['ぶたい','みゅーじかるかんげき', 'レトロ（ファッション・めぐり・しゅうしゅう）', 'どうぶつのあかちゃんをみること！！'],
                'とくぎ': ['いらすと（#はなすと・10びょうにがおえも！)','しょどう'],
            }],
            'おとしまりさ': [self.おとしまりさ,{
                'けつえきがた': 'B',
                'せいざ': 'ししざ',
                'しんちょう': '160cm',
                'せいねんがっぴ': '1998-8-11',
                'しゅっしんち': 'ふくおかけん',
                'しゅみ': ['にんげんかんさつ', 'コスメをあつめること', 'たべあるき'],
                'とくぎ': ['フラフープ', 'ファンのかたのなまえをおぼえる', 'ふくおか愛をかたる'],
            }],
            'さいとうきあら': [self.さいとうきあら,{
                'けつえきがた': 'B',
                'せいざ': 'いてざ',
                'しんちょう': '156.2cm',
                'せいねんがっぴ': '2004-11-26',
                'しゅっしんち': 'とちぎけん',
                'しゅみ': ['げーむ','からおけにいく','メイクどうがなどみてまねする'],
                'とくぎ': ['たちブリッチ','すうびょうをあたまの中ではかる','ドラえもんとまさおくんのものまね'],
            }],
            'ささきまいか': [self.ささきまいか,{
                'けつえきがた': 'A',
                'せいざ': 'みずがめざ',
                'しんちょう': '157cm',
                'せいねんがっぴ': '2000-1-21',
                'しゅっしんち': 'あいちけん',
                'しゅみ': ['ねること'],
                'とくぎ': ['からまったネックレスぜったいほどける'],
            }],
            'たかまつひとみ': [self.たかまつひとみ,{
                'けつえきがた': 'AB',
                'せいざ': 'やぎざ',
                'しんちょう': '163cm',
                'せいねんがっぴ': '2001-1-19',
                'しゅっしんち': 'とうきょうと',
                'しゅみ': ['えいが', 'どらま鑑賞'],
                'とくぎ': ['バトントワリング'],
            }],
            'たきわきしょうこ': [self.たきわきしょうこ,{
                'けつえきがた': 'O',
                'せいざ': 'かにざ',
                'しんちょう': '158cm',
                'せいねんがっぴ': '2001-7-9',
                'しゅっしんち': 'かながわけん',
                'しゅみ': ['りょうり', 'ヘアアレンジ', 'よこはまさんさく', 'カフェめぐり'],
                'とくぎ': ['マラソン'],
            }],
            'のぐちいおり': [self.のぐちいおり,{
                'けつえきがた': 'O',
                'せいざ': 'おうしざ',
                'しんちょう': '161cm',
                'せいねんがっぴ': '2000-4-26',
                'しゅっしんち': 'いばらきけん',
                'しゅみ': ['あにめまんがげーむ','どうがかんしょう'],
                'とくぎ': ['とくにない！！'],
            }],
            'もろはしさな': [self.もろはしさな,{
                'けつえきがた': 'B',
                'せいざ': 'ししざ',
                'しんちょう': '158cm',
                'せいねんがっぴ': '1996-8-3',
                'しゅっしんち': 'ふくしまけん',
                'しゅみ': ['ふらだんす', 'タヒチアンダンス'],
                'とくぎ': ['すいえいえいりょくけんてい2級'],
            }],
            'やまもとあんな': [self.やまもとあんな,{
                'けつえきがた': 'A',
                'せいざ': 'いてざ',
                'しんちょう': '149.5cm',
                'せいねんがっぴ': '1997-11-30',
                'しゅっしんち': 'ひろしまけん',
                'しゅみ': ['すぽーつかんせん（やきゅう、サッカー、バレー）','ダンス','りょうり'],
                'とくぎ': ['目分量料理']
            }],
        }

        self.モード一覧 = 0
        self.モードメンバ = 1

        self.rpg = rpg
        self.list = []

        for key in list(self.メンバープロフィール.keys()):
            self.list.append([key, self.メンバープロフィール[key][0]])

        self.member = Menu(
            const.色.BLUE.value,
            const.色.WHITE.value,
            const.色.DEEP_BLUE.value,
            self.list
        )
        self.list.append(("メニューに戻る", self.メニューに戻る))

        self.モード = self.モード一覧
        self.選択したメンバー = None
        self.メニューIdx = 0

    def メニューに戻る(self):
        self.rpg.change_story(const.STORY.TITLE)

    def おおたにえみり(self):
        self.モード = self.モードメンバ
        self.選択("おおたにえみり")

    def おおばはな(self):
        self.モード = self.モードメンバ
        self.選択("おおばはな")

    def おとしまりさ(self):
        self.モード = self.モードメンバ
        self.選択("おとしまりさ")

    def さいとうきあら(self):
        self.モード = self.モードメンバ
        self.選択("さいとうきあら")

    def ささきまいか(self):
        self.モード = self.モードメンバ
        self.選択("ささきまいか")

    def たかまつひとみ(self):
        self.モード = self.モードメンバ
        self.選択("たかまつひとみ")

    def たきわきしょうこ(self):
        self.モード = self.モードメンバ
        self.選択("たきわきしょうこ")

    def のぐちいおり(self):
        self.モード = self.モードメンバ
        self.選択("のぐちいおり")

    def もろはしさな(self):
        self.モード = self.モードメンバ
        self.選択("もろはしさな")

    def やまもとあんな(self):
        self.モード = self.モードメンバ
        self.選択("やまもとあんな")

    def 選択(self, メンバー名):
        self.選択したメンバー = メンバー名

    def start(self):
        if const.DEBUG:
            print("Book.start()")

    def update(self):
        match self.モード:
            case self.モード一覧:
                self.member.update()
            case self.モードメンバ:
                if self.メニューIdx == 0:
                    pass
                elif self.メニューIdx == 1:
                    pass
                elif self.メニューIdx == 2:
                    pass

                if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                    if self.メニューIdx == 1 or self.メニューIdx == 2:
                        pyxel.play(const.BGMチャンネル, [const.メニュー音])
                        self.メニューIdx -= 1
                if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                    if self.メニューIdx == 0 or self.メニューIdx == 1:
                        pyxel.play(const.BGMチャンネル, [const.メニュー音])
                        self.メニューIdx += 1

                if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
                    pyxel.play(const.BGMチャンネル, [const.メニュー音])
                    index =  list(self.メンバープロフィール.keys()).index(self.選択したメンバー)
                    if self.メニューIdx == 0:
                        if index == 0:
                            return
                        else:
                            name = list(self.メンバープロフィール.keys())[index - 1]
                            self.選択(name)
                    elif self.メニューIdx == 1:
                        self.モード = self.モード一覧
                    elif self.メニューIdx == 2:
                        if index == len(self.メンバープロフィール) - 1:
                            return
                        else:
                            name = list(self.メンバープロフィール.keys())[index + 1]
                            self.選択(name)

    def draw(self):
        match self.モード:
            case self.モード一覧:
                self.member.draw()
            case self.モードメンバ:
                pyxel.cls(0)
                pyxel.text(10, 10, "メンバー紹介", 7, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                
                #なまえ
                pyxel.rectb(10, 20, 80, 20, const.色.WHITE.value)
                pyxel.text(15, 25,  self.選択したメンバー, 7, pyxel.Font('assets/misaki_gothic_2nd.bdf'))

                #どっと
                pyxel.rectb(100, 20, 65, 20, const.色.WHITE.value)
                if 0 < pyxel.frame_count % 10 and  pyxel.frame_count % 10 < 5:
                    pyxel.blt(100,22,0,
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['右'][const.向き.南][0],
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['右'][const.向き.南][1],
                        const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)
                else:
                    pyxel.blt(100,22,0,
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['左'][const.向き.南][0],
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['左'][const.向き.南][1],
                        const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)
                if 0 < pyxel.frame_count % 10 and  pyxel.frame_count % 10 < 5:
                    pyxel.blt(116,22,0,
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['右'][const.向き.東][0],
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['右'][const.向き.東][1],
                        const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)
                else:
                    pyxel.blt(116,22,0,
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['左'][const.向き.東][0],
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['左'][const.向き.東][1],
                        const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)
                if 0 < pyxel.frame_count % 10 and  pyxel.frame_count % 10 < 5:
                    pyxel.blt(132,22,0,
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['右'][const.向き.西][0],
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['右'][const.向き.西][1],
                        const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)
                else:
                    pyxel.blt(132,22,0,
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['左'][const.向き.西][0],
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['左'][const.向き.西][1],
                        const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)
                if 0 < pyxel.frame_count % 10 and  pyxel.frame_count % 10 < 5:
                    pyxel.blt(148,22,0,
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['右'][const.向き.北][0],
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['右'][const.向き.北][1],
                        const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)
                else:
                    pyxel.blt(148,22,0,
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['左'][const.向き.北][0],
                        const.キャラ[self.キャラ名コンバート(self.選択したメンバー)]['左'][const.向き.北][1],
                        const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)

                pyxel.text(190, 25, "<<", const.色.RED.value if self.メニューIdx == 0 else const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                pyxel.text(205, 25, "戻る", const.色.RED.value if self.メニューIdx == 1 else const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                pyxel.text(230, 25, ">>", const.色.RED.value if self.メニューIdx == 2 else const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))

                #ぷろふ
                pyxel.rectb(10, 50, 236, 196, const.色.WHITE.value)
                cnt = 0
                for i, (key, value) in enumerate(self.メンバープロフィール[self.選択したメンバー][1].items()):
                    if key == 'しゅみ':
                        for j, hobby in enumerate(value):
                            if j == 0:
                                pyxel.text(15, 65 + cnt * 15, f"{key}: {hobby}", const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                            else:
                                pyxel.text(15, 65 + cnt * 15, f"     : {hobby}", const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                            cnt += 1
                    elif key == 'とくぎ':
                        for j, skill in enumerate(value):
                            if j == 0:
                                pyxel.text(15, 65 + cnt * 15, f"{key}: {skill}", const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                            else:
                                pyxel.text(15, 65 + cnt * 15, f"     : {skill}", const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                            cnt += 1
                    else:
                        pyxel.text(15, 65 + cnt * 15, f"{key}: {value}", const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
                        cnt += 1

    def キャラ名コンバート(self, name):
        if name == "おおたにえみり":
            return "みりにゃ"
        elif name == "おおばはな":
            return "はなちゃん"
        elif name == "おとしまりさ":
            return "りさ"
        elif name == "さいとうきあら":
            return "きあら"
        elif name == "ささきまいか":
            return "まいか"
        elif name == "たかまつひとみ":
            return "ひとみ"
        elif name == "たきわきしょうこ":
            return "しょこ"
        elif name == "のぐちいおり":
            return "いおり"
        elif name == "もろはしさな":
            return "さなつん"
        elif name == "やまもとあんな":
            return "あんな"