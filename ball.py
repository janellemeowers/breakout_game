from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # ball speed
        self.move_speed = .05
        self.reset_position()

    # ball moves by 10
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            #reverse horiz direction, go in opposite direction, so neg
            self.x_move *= -1
        if y_bounce:
            #reverse vertical
            self.y_move *= -1

    def reset_position(self):
        # go center
        self.goto(0, -240)
        #move up
        self.y_move_dist = -10