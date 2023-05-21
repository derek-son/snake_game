from turtle import Turtle
import pandas as pd
import random

# colors
DF = pd.read_excel("C:\\Users\\dson1\\Downloads\\tk-colours.xlsx")
COLORS = DF['Name'].values.tolist()

# directions
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake(Turtle):

    def __init__(self):
        super().__init__()

        self.snake_speed = 20
        self.starting_snake_length = 3
        self.shape("circle")
        self.color("white")
        self.speed("normal")
        self.penup()

        self.main_snek = []
        self.main_snek.append(self)
        self.head = self.main_snek[0]

        for n in range(self.starting_snake_length - 1):
            self.grow()

    def grow(self):
        last_segment = self.main_snek[-1]
        new_segment = last_segment.clone()
        # new_segment.color(COLORS[random.randrange(0, len(COLORS) - 1)])  # Changes color of each new snake block
        new_segment.showturtle()
        self.main_snek.append(new_segment)
        return new_segment

    def move(self):
        for segment in range(len(self.main_snek) - 1, 0, -1):  # tail follows head (easier turns)
            new_x = self.main_snek[segment - 1].xcor()
            new_y = self.main_snek[segment - 1].ycor()
            self.main_snek[segment].setpos(new_x, new_y)
        self.head.forward(self.snake_speed)  # move snake head

    def collision_check(self, spawn_dimension):
        if self.head.xcor() > spawn_dimension \
                or self.head.xcor() < -1 * spawn_dimension \
                or self.head.ycor() > spawn_dimension \
                or self.head.ycor() < -1 * spawn_dimension:
            return False
        for body_part in self.main_snek[3:]:
            if self.head.distance(body_part) < 9:
                return False
        else:
            return True

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
