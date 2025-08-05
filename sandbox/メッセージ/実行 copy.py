import pyxel
import os
import sys
sys.path.append(os.getcwd())
from model.message import Message
import const

class メッセージ実行:
    def __init__(self):
        pyxel.init(256,256,"message")
        pyxel.cls(7)
        self.message = Message()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.message.話す(const.M_TYPE.WINDOW,
                        "まいか",["きあらちゃーん", "あそぼー"])
        # self.message.話す(const.M_TYPE.WINDOW,
        #                 "きあら",["あ！まいかちゃん","ねえねえ今日ってさー"])
    
    def draw(self):
        self.message.表示()

メッセージ実行()