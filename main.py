"""
TODO: 1. Create Snake body w/ 3 squares DONE
TODO: 2. move snake continuously forwards DONE
TODO: 3. How to control the snake using keyboard controls DONE
TODO: 4. Detect collision with food --> new food created in random location
TODO: 5. Add to snake's body (score + scoreboard [screen.title]) text in program w/ autoupdate
TODO: 6. Detect collision with wall (print Game over)
TODO: 7. Detect collision with tail
"""
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def start_game():
    screen = Screen()  # Creates canvas
    screen.bgcolor("black")
    screen_dimension = 500
    screen.setup(width=screen_dimension, height=screen_dimension)
    screen.title("Snake Game")
    screen.tracer(0)

    spawn_dimension = round((screen_dimension - 20) / 2, 0)
    snake = Snake()  # Calls Snake class
    food = Food(spawn_dimension)  # Calls Food class
    scoreboard = Scoreboard(spawn_dimension)  # Calls Scoreboard class

    screen.onkeypress(snake.right, "Right")  # Snake controls
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.down, "Down")
    screen.listen()

    game_ongoing = True  # Game state
    while game_ongoing:
        screen.update()  # refreshes screen
        time.sleep(.1)  # delays refresh frequency
        snake.move()
        game_ongoing = snake.collision_check(spawn_dimension)
        if snake.distance(food) < 15:
            snake.grow()
            food.spawn()
            scoreboard.add_point()

    scoreboard.game_over()
    screen.exitonclick()


start_game()
