from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1)
        self.color("red")
        self.speed(0)
        self.setheading(170)

    def change_direction(self,rp,lp):
        if self.ycor()>=370 or self.ycor()<=-370 :
            self.setheading(360-self.heading())
            return 0
        
        elif self.xcor()>=680 :
            if self.xcor()<=700 and self.ycor()>=rp and self.ycor()<=rp+80:
                self.setheading(540-self.heading())
                return 0
            elif self.xcor()>=+700 :
                self.goto(0,0)
                return -1
        elif self.xcor()<=-680 :
            if  self.ycor()>=lp and self.ycor()<=lp+80 and self.xcor()>= -700:
                self.setheading(540-self.heading())
                return 0
            elif self.xcor()<=-700 :
                self.goto(0,0)
                return 1