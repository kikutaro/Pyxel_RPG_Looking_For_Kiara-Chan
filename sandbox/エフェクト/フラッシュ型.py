import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Flash Effect")
        self.mode = "idle"  # 'idle', 'flash', 'fade'
        self.timer = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.mode = "flash"
            self.timer = 0

        if self.mode == "flash":
            self.timer += 1
            if self.timer > 5:
                self.mode = "fade"
                self.timer = 0

        elif self.mode == "fade":
            self.timer += 1
            if self.timer > 30:
                self.mode = "idle"
                self.timer = 0

    def draw(self):
        pyxel.cls(1)  # 背景（例として青）

        pyxel.text(40, 50, "SPACE: Flash Effect", 7)

        if self.mode == "flash":
            pyxel.rect(0, 0, pyxel.width, pyxel.height, 7)  # 白フラッシュ（色7）
        elif self.mode == "fade":
            # 黒を徐々に重ねる（不透明度のないPyxelなので段階的に濃くする）
            darkness = min(self.timer * 8, 15)
            pyxel.rect(0, 0, pyxel.width, pyxel.height, 0)

App()