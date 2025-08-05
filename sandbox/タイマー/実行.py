import pyxel
import os
import sys
sys.path.append(os.getcwd())
from model.timer import Timer

class タイマー:
    def __init__(self):
        pyxel.init(256,256,"タイマー")

        self.timer = Timer()
        self.timer.経過時間 = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.timer.経過時間 < 10:
            self.timer.経過時間 += 1
        else:
            pyxel.quit()

    def draw(self):
        self.timer.表示()

タイマー()