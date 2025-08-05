import pyxel
import os
import sys
sys.path.append(os.getcwd())
import const

class App:
    def __init__(self):
        pyxel.init(256, 256, title="DQ-style Message")
        self.full_message = "こんにちは！勇者よ、旅の準備はできているか？"
        self.displayed_message = ""
        self.char_index = 0
        self.frame_counter = 0
        self.speed = 2  # 小さいほど速く表示される
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.char_index < len(self.full_message):
            self.frame_counter += 1
            if self.frame_counter >= self.speed:
                self.displayed_message += self.full_message[self.char_index]
                self.char_index += 1
                self.frame_counter = 0
        else:
            # Zキーでリセット
            if pyxel.btnp(pyxel.KEY_Z):
                self.char_index = 0
                self.displayed_message = ""

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(8, 80, 144, 32, 7)  # メッセージウィンドウ風
        pyxel.rectb(8, 80, 144, 32, 0)
        pyxel.text(12, 88, self.displayed_message, 0, const.MESSAGE_FONT)

App()