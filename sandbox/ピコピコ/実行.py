import pyxel

class 実行:
    def __init__(self):
        pyxel.init(128,128,"キャラクターピコピコ歩き")
        pyxel.load('../../my_resource.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(7)
        pyxel.text(0,0, str(pyxel.frame_count), 0)
        if 0 < pyxel.frame_count % 10 and  pyxel.frame_count % 10 < 5:
            pyxel.blt(128 / 2 - 16 /2,128 / 2 - 16/2,0,0,0,16,16)
        else:
            pyxel.blt(128 / 2 - 16/2,128 / 2 - 16/2,0,0,16,16,16)

実行()