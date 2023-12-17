from turtle import Turtle

class Paddle():
    def __init__(self,position):
        self.segments=[]
        if position=="right":
            p=1
        else:
            p=-1
        for i in range(4):
            new_segments=Turtle("square")
            new_segments.penup()
            new_segments.color("black")
            new_segments.goto(p*700,-40+i*20)
            new_segments.setheading(90)
            self.segments.append(new_segments)

    def up(self):
        if self.segments[3].ycor()<345:
            for seg in self.segments:
                seg.forward(60)

    def down(self):
        if self.segments[0].ycor()> -345:
            for seg in self.segments:
                seg.backward(60)
    def get_min_ypos(self):
        return self.segments[0].ycor()