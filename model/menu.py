import pyxel
import const

# list [ taple (label, function)]
class Menu:
    def __init__(self, 背景色, 文字色, 選択色, メニュー):
        self.背景色 = 背景色
        self.文字色 = 文字色
        self.選択色 = 選択色
        self.menu = メニュー
        self.selected_index = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP):
            pyxel.play(const.BGMチャンネル, [const.メニュー音])
            self.selected_index = (self.selected_index - 1) % len(self.menu)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            pyxel.play(const.BGMチャンネル, [const.メニュー音])
            self.selected_index = (self.selected_index + 1) % len(self.menu)
        elif pyxel.btnp(pyxel.KEY_RETURN):
            self.menu[self.selected_index][1]()

    def draw(self):
        if self.背景色 is not None:
            pyxel.cls(self.背景色)

        メニューで一番長い文字 = len(max(self.menu, key=lambda x: len(x[0]))[0])
        メニューの行数 = len(self.menu)

        メニュー開始位置X = (const.FIELD - メニューで一番長い文字 * const.FONT_SIZE) / 2
        メニューの開始位置Y = (const.FIELD - メニューの行数 * const.メニュー縦幅) / 2

        for idx, val in enumerate(self.menu):
            if idx == self.selected_index:
                pyxel.text(メニュー開始位置X - const.FONT_SIZE, メニューの開始位置Y + idx *const.メニュー縦幅, ">", self.選択色, const.SUBTITLE_FONT)
                pyxel.text(メニュー開始位置X, メニューの開始位置Y + idx * const.メニュー縦幅, val[0], self.選択色, const.SUBTITLE_FONT)
            else:
                pyxel.text(メニュー開始位置X, メニューの開始位置Y + idx * const.メニュー縦幅, " ", self.文字色, const.SUBTITLE_FONT)
                pyxel.text(メニュー開始位置X, メニューの開始位置Y + idx * const.メニュー縦幅, val[0], self.文字色, const.SUBTITLE_FONT)