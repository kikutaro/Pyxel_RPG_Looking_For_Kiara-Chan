# title: Looking for Kiara-chan!
# author: IKOMAI
# desc: for fun for =LOVE fan
# site: https://equal-maika.jp/
# license: MIT
# version: 1.0

import pyxel
import const
from story import Title, Bgm, Opening, Play, Book, PlayQuiz, Ending, Gameclear

# RPG本体
class RPG:
    def __init__(self):
        if const.DEBUG:
            print("RPG.__init__")

        # ウィンドウ初期化
        pyxel.init(const.L_WIDTH, const.L_HEIGHT, title=const.TITLE)
        # リソース読み込み
        pyxel.load('my_resource.pyxres')
        
        # 物語オブジェクトの管理
        # これにより、物語ごとにstartやupdate,drawを呼び出すことができる
        self.story_manager = {
            const.STORY.TITLE : Title(self),
            const.STORY.BGM : Bgm(self),
            const.STORY.OPENING : Opening(self),
            const.STORY.PLAY : Play(self),
            const.STORY.BOOK : Book(self),
            const.STORY.QUIZ : PlayQuiz(self),
            const.STORY.ENDING : Ending(self),
            const.STORY.GAMECLEAR : Gameclear(self)
        }
        # まずはタイトルから
        self.change_story(const.STORY.TITLE)

        pyxel.run(self.update, self.draw)

    # 物語の切り替え
    def change_story(self, story):
        if const.DEBUG:
            print("RPG.change_story")

        self.story = story
        self.story_manager[self.story].start()

    # 物語のupdate
    def update(self):
        self.story_manager[self.story].update()

    # 物語のdraw
    def draw(self):
        self.story_manager[self.story].draw()

RPG()