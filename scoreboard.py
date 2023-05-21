from turtle import Turtle

SCORE = 0


class Scoreboard(Turtle):
    def __init__(self, spawn_dim):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, spawn_dim - 10)
        self.write("Score: " + str(self.score), move=False, align="center", font=("Courier", 14, "normal"))

    def add_point(self):
        self.clear()
        self.score += 1
        self.write("Score: " + str(self.score), move=False, align="center", font=("Courier", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Courier", 14, "normal"))
