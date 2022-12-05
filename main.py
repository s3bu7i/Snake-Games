
import random
import time
from turtle import Screen, Turtle
#from Python.projects.scoreboard import Scoreboard
#from Python.projects.snake import UP
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from drawline import Drawer


screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
drawer = Drawer()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True    

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor()>281 or snake.head.xcor()<-281 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboard.gameover()
        game_is_on = False
    
    for segment in snake.segment[1:]:
        
        if snake.head.distance(segment) < 15:
            scoreboard.gameover()
            game_is_on = False
     
screen.mainloop()
