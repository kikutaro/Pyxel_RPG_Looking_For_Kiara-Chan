import pyxel

class 実行:
    def __init__(self):
        pyxel.init(1024,1024,"マップビューア")
        # pyxel.init(1280,1280,"マップビューア")
        pyxel.load('../../my_resource.pyxres')

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.bltm(0,0,0,0,0,1280,1280)
        for i in range(0, 1280, 256):
            pyxel.line(i, 0, i, 1280, 0)
            pyxel.line(0, i, 1280, i, 0)

実行()