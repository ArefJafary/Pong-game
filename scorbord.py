from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score=0
        self.l_score=0
        self.hideturtle()
        self.penup()
        self.goto(0,347)
        self.color("black")
        self.update()
        

    def update(self):
        self.clear()
        self.write(f"{self.l_score}      {self.r_score}",move=False,align="center",font=('Arial', 28, 'normal'))


    def increase_score(self, score):
        if score==1:
            self.r_score+=1
        else:
            self.l_score+=1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game over",move=False,align="center",font=('Arial', 50, 'normal'))
