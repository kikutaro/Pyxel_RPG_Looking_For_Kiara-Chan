import pyxel
import const
import math

class Timer:
    def __init__(self):
        self.経過時間= None
        self.m_font = pyxel.Font('assets/misaki_gothic_2nd.bdf')
        self.はじまりのとき = None

    def カウントスタート(self):
        self.はじまりのとき = pyxel.frame_count

    def 表示(self):
        pyxel.rect(const.T_POS_X, const.T_POS_Y, const.T_WIDTH, const.T_HEIGHT, const.色.RED.value)
        self.経過時間 = math.floor((pyxel.frame_count - self.はじまりのとき) / 30)
        pyxel.text(const.T_POS_X + const.T_PADDING, const.T_POS_Y + const.T_PADDING, str(self.経過時間) + " 秒", const.色.WHITE.value, self.m_font)