import pyxel
import const
from model.quiz import Quiz
from model.music import Music

class PlayQuiz:
    def __init__(self, rpg):
        self.music = Music()
        self.quiz = Quiz(rpg)

    def start(self):
        self.music.play_LOVE()

    def update(self):
        self.quiz.回答する()

    def draw(self):
        self.quiz.draw()