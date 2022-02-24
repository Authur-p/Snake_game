from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
filename = 'data.txt'

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('                                                             My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
   # with open(filename, 'r') as file:
    #    scoreboard.score = file.read()

    # detect collision with food
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()


screen.exitonclick()
