import pyxel
import random
import math

class Dot:
    def __init__(self, x, y):
        self.origin_x = x
        self.origin_y = y
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(20, 50)
        self.x = x + math.cos(angle) * distance
        self.y = y + math.sin(angle) * distance
        self.vx = (x - self.x) / 60
        self.vy = (y - self.y) / 60
        self.frame = 0
        self.max_frame = 60

    def update(self):
        if self.frame < self.max_frame:
            self.x += self.vx
            self.y += self.vy
            self.frame += 1

    def draw(self):
        pyxel.pset(int(self.x), int(self.y), 7)

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Game Over Effect")
        pyxel.images[0].cls(0)
        pyxel.images[0].text(30, 50, "GAME OVER", 7)

        # ドット抽出
        self.dots = []
        for y in range(120):
            for x in range(160):
                if pyxel.image(0).pget(x, y) == 7:
                    self.dots.append(Dot(x, y))

        self.frame = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.frame += 1
        for dot in self.dots:
            dot.update()

    def draw(self):
        pyxel.cls(0)
        for dot in self.dots:
            dot.draw()

App()
