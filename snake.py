

from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT =180


class Snake:
    def __init__(self):
        self.segment = []
        self.creat_snake()
        self.head = self.segment[0]
    
    def creat_snake(self):
        for position in POSITIONS:
           self.add_segment(position) 

    def add_segment(self,position):
        new_segment = Turtle(shape = "square")
        new_segment.penup()
        new_segment.color("red")
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())
        
    def move(self):
        for seg_number in range(len(self.segment)-1,0,-1):
            new_x = self.segment[seg_number-1].xcor()
            new_y = self.segment[seg_number-1].ycor()
            self.segment[seg_number].goto(new_x, new_y)

        self.head.forward(DISTANCE)
        
    def up(self):
        if self.head.heading()!=DOWN:
            if self.head.xcor() - self.segment[1].xcor() > 19 or self.head.xcor() - self.segment[1].xcor() < -19:
                self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            if self.head.xcor() - self.segment[1].xcor() > 19 or self.head.xcor() - self.segment[1].xcor() < -19:
                self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            if self.head.ycor() - self.segment[1].ycor() > 19 or self.head.ycor() - self.segment[1].ycor() < -19:
                self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading()!=LEFT:
            if self.head.ycor() - self.segment[1].ycor() > 19 or self.head.ycor() - self.segment[1].ycor() < -19:
                self.head.setheading(RIGHT)
        
    