import pyxel
import const
from model.music import Music
from model.menu import Menu

class Bgm:
    def __init__(self, rpg):
        self.rpg = rpg
        self.music = Music()
        self.menu = Menu(
            const.色.BLACK.value,
            const.色.WHITE.value,
            const.色.RED.value,
            self.music.music_list)
        self.music.music_list.append(("メニューに戻る", self.メニューに戻る))

    def start(self):
        pass

    def update(self):
        self.menu.update()

    def draw(self):
        self.menu.draw()

    def メニューに戻る(self):
        pyxel.stop()
        self.rpg.change_story(const.STORY.TITLE)