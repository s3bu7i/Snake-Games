
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.type_score()
        
    def type_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial",22,"normal"))
        
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.type_score()
        
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Arial",22,"normal"))
            
