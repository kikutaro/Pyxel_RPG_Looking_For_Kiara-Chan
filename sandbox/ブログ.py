import pyxel

class ブログ:
    def __init__(self):
        pyxel.init(256,256,"ブログ用")

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(7)
        pyxel.text(0,0,"Hello!",0)
        pyxel.text(100,0,"こんにちは",0)

ブログ()