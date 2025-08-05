import pyxel
import const
from model.music import Music
from model.menu import Menu

class Bgm:
    def __init__(self, rpg):
        if const.DEBUG:
            print("Bgm.__init__")

        self.rpg = rpg
        self.music = Music()
        self.menu = Menu(
            const.色.BLACK.value,
            const.色.WHITE.value,
            const.色.RED.value,
            self.music.music_list)
        self.music.music_list.append(("メニューに戻る", self.メニューに戻る))

    def start(self):
        if const.DEBUG:
            print("Bgm.start()")

    def update(self):
        self.menu.update()

    def draw(self):
        self.menu.draw()

    def メニューに戻る(self):
        self.rpg.change_story(const.STORY.TITLE)