from turtle import Turtle

# inherit turtle class
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=8)
        self.penup()
        self.goto(0, -300)

    def go_right(self):
        # move 20 from current x
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
