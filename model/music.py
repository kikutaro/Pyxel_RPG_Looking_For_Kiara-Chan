import pyxel
import const
import random

class Music:
    def __init__(self):
        self.num = -1
        self.music_list = [
            ["樹愛羅助けに来たぞ", self.play_樹愛羅助けに来たぞ],
            ["＝LOVE", self.play_LOVE],
            ["探せダイヤモンドリリー1", self.play_探せダイヤモンドリリー1],
            ["探せダイヤモンドリリー2", self.play_探せダイヤモンドリリー2],
            ["真夜中マーメイド", self.play_真夜中マーメイド],
            ["この空がトリガー", self.play_この空がトリガー],
            ["しゅきぴ", self.play_しゅきぴ],
            ["絶対アイドル辞めないで", self.play_絶対アイドル辞めないで],
            ["仲直りシュークリーム", self.play_仲直りシュークリーム],
            ["とくべチュして", self.play_とくべチュして],
            ["ナツマトペ", self.play_ナツマトペ],
            ["夏祭り恋慕う", self.play_夏祭り恋慕う],
            ["お姫様にしてよ", self.play_お姫様にしてよ],
            ["あの子コンプレックス", self.play_あの子コンプレックス],
            ["僕らの制服クリスマス", self.play_僕らの制服クリスマス],
        ]

    def play_樹愛羅助けに来たぞ(self):
        pyxel.playm(0, loop=True)

    def play_LOVE(self):
        pyxel.playm(1, loop=True)

    def play_探せダイヤモンドリリー1(self):
        pyxel.playm(2, loop=True)

    def play_探せダイヤモンドリリー2(self):
        pyxel.playm(3, loop=True)

    def play_真夜中マーメイド(self):
        pyxel.play(0, [20, 21, 22])

    def play_この空がトリガー(self):
        pyxel.play(0, [23, 24, 25])

    def play_しゅきぴ(self):
        pyxel.play(0, [26,27])

    def play_超特急逃走中(self):
        pyxel.play(0, 28)

    def play_仲直りシュークリーム(self):
        pyxel.play(0, 29)

    def play_とくべチュして(self):
        pyxel.play(0, [30, 31])

    def play_ナツマトペ(self):
        pyxel.play(0, 32)

    def play_夏祭り恋慕う(self):
        pyxel.play(0, [33, 34])

    def play_ウィークエンドシトロン(self):
        pyxel.play(0, 35)

    #36抜け番

    def play_お姫様にしてよ(self):
        pyxel.play(0, [37, 38, 39])

    def play_あの子コンプレックス(self):
        pyxel.play(0, [40, 41, 42])

    def play_僕らの制服クリスマス(self):
        pyxel.play(0, [43, 44])

    def play_虹の素(self):
        pyxel.play(0, 46)

    def play_海とレモンティー(self):
        pyxel.play(0, [47, 48])

    def play_呪って呪って(self):
        pyxel.play(0, [49, 50])

    def play_絶対アイドル辞めないで(self):
        pyxel.play(0, [54,55]) 

    def play_イコラブ沼(self):
        pyxel.play(0, 59)

    #ややこしいがBGMはconstで定義、上のリストは全曲リスト
    def BGMランダム再生(self):
        self.num = random.randint(0, len(const.BGM) -1)
        pyxel.play(0, const.BGM[self.num][1], loop=True)

    def BGM名取得(self):
        if self.num == -1:
            return "音なし"
        else:
            return const.BGM[self.num][0]
    
    def BGM名表示(self):
        pyxel.rect(const.B_POS_X, const.B_POS_Y, const.B_WIDTH, const.B_HEIGHT, const.色.BLUE.value)
        if self.num != -1:
            pyxel.text(const.B_POS_X + const.T_PADDING, const.B_POS_Y + const.T_PADDING, self.BGM名取得(), const.色.WHITE.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))