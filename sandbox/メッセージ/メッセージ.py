import pyxel

class メッセージ:
    def __init__(self):
        self.話者 = None
        self.メッセージ = []
        self.行 = 0
        self.表示位置 = 0

        self.日本語フォント = pyxel.Font("../../assets/misaki_gothic_2nd.bdf")

    def 話す(self, 話者, メッセージ):
        self.話者 = 話者
        self.メッセージ = メッセージ

        #メッセージを1文字ずつ表示
        if pyxel.frame_count % 5 == 0:
            self.表示位置 += 1

        #複数行あるときはEnterで次の行を表示
        if pyxel.btnp(pyxel.KEY_RETURN):
            if len(self.メッセージ) >= self.行 + 1:
                self.表示位置 = 0
                if self.行 + 1 < len(self.メッセージ):
                    self.行 += 1

    def メッセージを表示する(self):
        #ウィンドウ
        pyxel.rect(10, 200, 256 - 10 - 10 , 50, 0)
        #話者
        pyxel.text(10, 190, self.話者, 0, self.日本語フォント)
        #会話
        for 文 in range(0, self.行):
            pyxel.text(15, 205 + 16 * 文, self.メッセージ[文], 7, self.日本語フォント)
        pyxel.text(15, 205 + 16 * self.行, self.メッセージ[self.行][0:self.表示位置], 7, self.日本語フォント)