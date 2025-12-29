from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.listen()
# screen = Screen()
# screen.listen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
jimmy = Turtle()
jimmy.color("white")
jimmy.hideturtle()
jimmy.write("Click Spacebar to Start!!!", align="center", font=24)
screen.tracer(0)

tim = Turtle()
tim.color("white")
tim.hideturtle()
tim.up()
tim.goto(-250, 250)
tim.down()
for i in range(4):
    tim.forward(250 * 2)
    tim.right(90)

screen.update()

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def start_game():
    global snake
    game_on = True
    snake_list = snake.list_of_segments
    while game_on:
        jimmy.clear()
        screen.update()
        time.sleep(0.1)
        if snake_list[0].distance(food) < 15:
            snake.extend_snake()
            food.food_move()
            scoreboard.increase_score()
        snake.move_snake()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")
        for all_segments in snake_list[1:len(snake_list)]:
            if snake_list[0].distance(all_segments) < 10:
                game_on = False
                jimmy.write("Game Over!! Enter Space to Play Again", align="center", font=24)
                scoreboard.reset_score()
                snake.snake_reset()
                snake = Snake()
        if -250 < snake_list[0].xcor() < 250 and -250 < snake_list[0].ycor() < 250:
            continue
        else:
            jimmy.write("Game Over!! Enter Space to Play Again", align="center", font=24)
            scoreboard.reset_score()
            snake.snake_reset()
            snake = Snake()
            game_on = False


screen.onkey(start_game, "space")

screen.exitonclick()
