import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.frame = 0
        self.effect_active = True
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.effect_active:
            self.frame += 1
            if self.frame > 60:  # エフェクト終了
                self.effect_active = False

    def draw(self):
        pyxel.cls(5)

        # 背景として何か表示（フィールドなど）
        pyxel.text(60, 55, "フィールド", 7)

        if self.effect_active:
            self.draw_expanding_circle()
            # self.draw_spiral(self.frame)

    def draw_expanding_circle(self):
        cx = pyxel.width // 2
        cy = pyxel.height // 2
        max_radius = math.hypot(cx, cy)
        radius = (self.frame / 60) * max_radius

        # 黒い円を描く（大きくなる）
        for y in range(pyxel.height):
            for x in range(pyxel.width):
                dist = math.hypot(x - cx, y - cy)
                if dist < radius:
                    pyxel.pset(x, y, 0)

    def draw_spiral(self,frame):
        cx, cy = pyxel.width // 2, pyxel.height // 2
        for i in range(100):
            angle = i * 0.3 + frame * 0.1
            radius = i
            x = int(cx + math.cos(angle) * radius)
            y = int(cy + math.sin(angle) * radius)
            if 0 <= x < pyxel.width and 0 <= y < pyxel.height:
                pyxel.pset(x, y, 7)


App()