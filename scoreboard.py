from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        #initial score
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        # clear before new scores
        self.clear()

        # for right side
        self.goto(550, 250)
        self.write(self.score, align="center", font=("Courier", 40, "normal"))

    def inc_point(self):
        self.score+=1
        self.update_scoreboard()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()

