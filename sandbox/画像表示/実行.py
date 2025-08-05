import pyxel

class 実行:
    def __init__(self):
        pyxel.init(256,256,"画像表示")
        # pyxel.load('../../my_resource.pyxres')
        self.img = pyxel.Image(64, 64)
        self.img.load(0, 0, '../../assets/ikomai_logo.png')
        # pyxel.user_data_dir("equal_maika", "kiara-chan-wo-sagase")

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(7)
        # pyxel.text(0,0,"hoge",8)
        pyxel.blt(0, 0, self.img, 0, 0, 64, 64, 0)

実行()