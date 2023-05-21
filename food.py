from turtle import Turtle
import random
from snake import Snake


class Food(Turtle):

    def __init__(self, spawn_dim):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("lightblue")
        self.spawn_dim = spawn_dim - 5
        self.spawn()

    def spawn(self):
        random_spawn_dim = random.randrange(self.spawn_dim * -1, self.spawn_dim, 20)
        self.setx(random_spawn_dim)
        self.sety(random_spawn_dim)
