import pyxel
import os
import sys
sys.path.append(os.getcwd())
import const

class 実行:
    def __init__(self):
        pyxel.init(256,256,"クリア")
        pyxel.load('../../my_resource.pyxres')

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(const.色.WHITE.value)
        mes1 = "さがしてくれて、ありがとう！"
        mes2 = "このスクリーンをキャプチャしてタイムをきそってね！"
        mes3 = "クリアタイム"
        pyxel.text(self.X軸センタリング(mes1, const.FONT_SIZE), 60, mes1, const.色.BLACK.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
        pyxel.text(self.X軸センタリング(mes2, const.FONT_SIZE), 80, mes2, const.色.BLACK.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))
        pyxel.text(self.X軸センタリング(mes3, const.FONT_SIZE), 100, mes3 , const.色.BLACK.value, pyxel.Font('assets/misaki_gothic_2nd.bdf'))

        #右
        if 0 < pyxel.frame_count % 10 and  pyxel.frame_count % 10 < 5:
            pyxel.blt((const.FIELD - const.キャラサイズ) / 2, (const.FIELD - const.キャラサイズ) / 2,0,
                const.キャラ['とくべちゅきあら']['右'][const.向き.南][0],
                const.キャラ['とくべちゅきあら']['右'][const.向き.南][1],
                const.キャラサイズ,const.キャラサイズ, const.色.WHITE.value)
        #左
        else:
            pyxel.blt((const.FIELD - const.キャラサイズ) / 2, (const.FIELD - const.キャラサイズ) / 2,0,
                const.キャラ['とくべちゅきあら']['左'][const.向き.南][0],
                const.キャラ['とくべちゅきあら']['左'][const.向き.南][1],
                const.キャラサイズ,const.キャラサイズ,const.色.WHITE.value)

        mes4 =  "　10秒"
        pyxel.text(self.X軸センタリング(mes4, const.TITLE_FONT_SIZE), 145, mes4, const.色.BLACK.value, pyxel.Font('assets/umplus_j12r.bdf'))

    def X軸センタリング(self, text, font_size):
        return ((const.FIELD - len(text) * font_size)) / 2

実行()