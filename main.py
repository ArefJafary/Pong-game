from turtle import Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from scorbord import Scoreboard
screen=Screen()
screen.setup(width=1500, height=780) #1400,750
screen.bgcolor("#92c6de")
screen.title("pong.RF")
screen.tracer(0)

l_paddle = Paddle("left")
r_paddle = Paddle("right")
ball=Ball()
scorbord=Scoreboard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on=True

while game_is_on:
    screen.update()
    x= ball.change_direction(r_paddle.get_min_ypos(), l_paddle.get_min_ypos())
    if x:
        scorbord.increase_score(x)
    ball.forward(1)
    sleep(0.00105)
    


















screen.exitonclick()