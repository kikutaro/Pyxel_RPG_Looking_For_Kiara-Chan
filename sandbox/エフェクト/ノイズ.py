import pyxel
import math
import random

class App: 
    def __init__(self):
        pyxel.init(160, 120, title="Noise Effect")
        self.mode = "idle"
        self.timer = 0
        self.noise_data = []
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.mode = "noise"
            self.timer = 0
            self.generate_noise()

        if self.mode == "noise":
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
        pyxel.cls(1)
        pyxel.text(40, 50, "SPACE: Noise Effect", 7)

        if self.mode == "noise":
            self.draw_noise()
        elif self.mode == "fade":
            pyxel.rect(0, 0, pyxel.width, pyxel.height, 0)

    def generate_noise(self):
        self.noise_data = [
            [random.randint(0, 15) for _ in range(pyxel.width // 2)]
            for _ in range(pyxel.height // 2)
        ]

    def draw_noise(self):
        for y, row in enumerate(self.noise_data):
            for x, col in enumerate(row):
                pyxel.pset(x * 2, y * 2, col)
                pyxel.pset(x * 2 + 1, y * 2, col)
                pyxel.pset(x * 2, y * 2 + 1, col)
                pyxel.pset(x * 2 + 1, y * 2 + 1, col)

App()