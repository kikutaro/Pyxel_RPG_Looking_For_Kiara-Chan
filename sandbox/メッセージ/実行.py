import pyxel
from メッセージ import メッセージ

class メッセージ実行:
    def __init__(self):
        pyxel.init(256,256,"message")
        pyxel.cls(7)
        self.メッセージ = メッセージ()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.メッセージ.話す("まいか", ["えっほ", "えっほ", "アンパンマンはつぶあんって伝えなきゃ"])
        # self.メッセージ.話す(["次のお話だよ"])
    def draw(self):
        self.メッセージ.メッセージを表示する()

メッセージ実行()