import pyxel
import os
import sys
sys.path.append(os.getcwd())
from model.____command import Command

class コマンド:
    def __init__(self):
        pyxel.init(256,256,"コマンド")
        pyxel.load('../my_resource.pyxres')

        self.command = Command(
            [
                ['うたう', 'あいてむ', 'みる','めも'],
                ['＝LOVE','にじのもと','まよなかマーメイド', 'しゅきぴ','夏祭り恋慕う','この空がトリガー','ぜったいアイドルやめないで','とくべちゅ、して'],
                ['ぬいぐるみ', 'あみもの', 'おけしょうせっと'],
                [''],
                ['りさ「きあらのようすがおかしい」','さな「きあら眠そうだったよね」']
            ]
        )

        pyxel.run(self.update, self.draw)

    def update(self):
        self.command.選択()

    def draw(self):
        pyxel.cls(0)
        self.command.表示()

コマンド()