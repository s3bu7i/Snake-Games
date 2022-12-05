
from turtle import Turtle, pendown

class Drawer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(290,0)
        self.pendown()
        self.goto(290,295)
        self.goto(-295,295)
        self.goto(-295,-290)
        self.goto(290,-290)
        self.goto(290,0)
        
        