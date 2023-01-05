from turtle import Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scoreboard import Scoreboard
import time
from turtle import Turtle

# SCREEN
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
#turn animation off, but you will need to refresh screen
screen.tracer(0)
screen.title("Breakout")
#title/win/lose text
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.color("white")
turtle.goto(-20, 250)
turtle.write("Breakout!", align='center', font=('Courier',40))

#paddle takes starting position
paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


game_is_on = True


def check_brick_collision():
    global ball, bricks, scoreboard

    for brick in bricks.bricks:
        #if less than 40 to brick
        if 40 > ball.distance(brick) > 0:
            scoreboard.inc_point()
            brick.clear()
            brick.goto(6000, 6000)
            bricks.bricks.remove(brick)

            # detect collision from left
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            # detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            # detect collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

while game_is_on:
    time.sleep(ball.move_speed)
    #refresh
    screen.update()
    ball.move()
    check_brick_collision()

    #COLLISION WITH L/R WALL
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)

    #COLLISION WITH TOP WALL
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)

    #COLLISION WITH BOTTOM = GAME OVER
    if ball.ycor() < -280:
        turtle.goto(0, -250)
        turtle.clear()
        turtle.write("You lose!", align='center', font=('Courier', 40))
        ball.reset()
        game_is_on = False

    #COLLISION WITH PADDLE
    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        paddle_x = paddle.xcor()
        ball_x = ball.xcor()
        # If Paddle is on Right of Screen
        if paddle_x > 0:
            if ball_x > paddle_x:
                # If ball hits paddles left side it, go left
                ball.bounce(x_bounce=True, y_bounce=True)

            else:
                ball.bounce(x_bounce=False, y_bounce=True)


        # If Paddle is left of Screen
        elif paddle_x < 0:
            if ball_x < paddle_x:
                # If ball hits paddles left side it, go left
                ball.bounce(x_bounce=True, y_bounce=True)
            else:
                ball.bounce(x_bounce=False, y_bounce=True)


        # Else Paddle is in the middle
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)

            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)

            else:
                ball.bounce(x_bounce=False, y_bounce=True)

    if len(bricks.bricks) == 0:
        turtle.goto(0, -250)
        turtle.clear()
        turtle.write("You win!", align='center', font=('Courier', 40))




screen.exitonclick()