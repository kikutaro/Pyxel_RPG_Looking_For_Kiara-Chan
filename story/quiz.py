import pyxel
import const
from model.quiz import Quiz
from model.music import Music

class PlayQuiz:
    def __init__(self, rpg):
        if const.DEBUG:
            print("Quiz.__init__")

        self.music = Music()
        self.quiz = Quiz(rpg)

    def start(self):
        if const.DEBUG:
            print("Quiz.start()")

        self.music.play_LOVE()

    def update(self):
        self.quiz.回答する()

    def draw(self):
        self.quiz.draw()