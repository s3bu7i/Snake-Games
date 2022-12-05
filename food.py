
from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.coordinates = []
        self.fill()
        self.refresh()
        
    def refresh(self):
        
        random_x = random.choice(self.coordinates)
        random_y = random.choice(self.coordinates)
        self.goto(random_x,random_y)
        
    def fill(self):
        for i in range(-260,260,20):
            self.coordinates.append(i)
        
        
        
        
        
        