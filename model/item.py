import pyxel
import const

class Item:
    def __init__(self):
        self.アイテム = []
        self.アイテム非表示 = False
        self.m_font = pyxel.Font('assets/misaki_gothic_2nd.bdf')

    def アイテムを追加(self, アイテム名):
        if アイテム名 not in self.アイテム and アイテム名 in const.アイテム:
            self.アイテム.append(アイテム名)

    def 表示(self):
        if len(self.アイテム) != 0 and not self.アイテム非表示:
            pyxel.rect(const.I_POS_X, const.I_POS_Y, const.I_WIDTH, const.I_HEIGHT, const.色.SKIN.value)
            pyxel.text(const.I_POS_X + const.T_PADDING, const.I_POS_Y + const.T_PADDING, "アイテム：", const.色.BLACK.value, self.m_font)
            pyxel.text(const.I_POS_X + const.T_PADDING + (len("アイテム：") * const.FONT_SIZE), const.I_POS_Y + const.T_PADDING, " ".join(self.アイテム), const.色.BLACK.value, self.m_font)