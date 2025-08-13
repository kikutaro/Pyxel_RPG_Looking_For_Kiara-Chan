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

        self.メニューで一番長い文字 = len(max(self.menu, key=lambda x: len(x[0]))[0])
        self.メニューの行数 = len(self.menu)

        self.メニュー開始位置X = (const.FIELD - self.メニューで一番長い文字 * const.FONT_SIZE) / 2
        self.メニューの開始位置Y = (const.FIELD - self.メニューの行数 * const.メニュー縦幅) / 2

        self.m_font = pyxel.Font('assets/misaki_gothic_2nd.bdf')

    def update(self):
        if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btnp(pyxel.KEY_UP):
            pyxel.play(const.BGMチャンネル, [const.メニュー音])
            self.selected_index = (self.selected_index - 1) % len(self.menu)
        elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btnp(pyxel.KEY_DOWN):
            pyxel.play(const.BGMチャンネル, [const.メニュー音])
            self.selected_index = (self.selected_index + 1) % len(self.menu)
        elif pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.KEY_RETURN):
            self.menu[self.selected_index][1]()

    def draw(self):
        if self.背景色 is not None:
            pyxel.cls(self.背景色)

        for idx, val in enumerate(self.menu):
            if idx == self.selected_index:
                pyxel.text(self.メニュー開始位置X - const.FONT_SIZE, self.メニューの開始位置Y + idx *const.メニュー縦幅, ">", self.選択色, self.m_font)
                pyxel.text(self.メニュー開始位置X, self.メニューの開始位置Y + idx * const.メニュー縦幅, val[0], self.選択色, self.m_font)
            else:
                pyxel.text(self.メニュー開始位置X, self.メニューの開始位置Y + idx * const.メニュー縦幅, " ", self.文字色, self.m_font)
                pyxel.text(self.メニュー開始位置X, self.メニューの開始位置Y + idx * const.メニュー縦幅, val[0], self.文字色, self.m_font)