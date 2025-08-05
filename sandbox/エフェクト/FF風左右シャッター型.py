import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Transition Effect")
        self.timer = 0
        self.transition = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):  # スペースでエフェクト開始
            self.transition = True
            self.timer = 0

        if self.transition:
            self.timer += 1
            if self.timer > 30:  # 30フレームで終了
                self.transition = False
                self.timer = 0

    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 50, "Press SPACE for effect!", 7)

        if self.transition:
            # シャッターが閉じていく演出（左右から黒い帯が出る）
            width = int(self.timer * pyxel.width / 60)
            pyxel.rect(0, 0, width, pyxel.height, 0)
            pyxel.rect(pyxel.width - width, 0, width, pyxel.height, 0)

App()