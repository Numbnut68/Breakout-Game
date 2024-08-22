# imports

from turtle import Screen, Turtle, write
from paddle import Paddle
from score import Scoreboard
from ball import Ball
import time
import random

# Initialize Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

#Initialize Paddle
paddle = Paddle((0, -250))

# Create and Initialize bricks
all_bricks_list = []
total_bricks = 39

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
def create_bricks():
    for row in range(4):
        y_cor = row * 30
        for column in range(10):
            new_brick = Turtle("square")
            new_brick.shapesize(stretch_len=3, stretch_wid=1)
            new_brick.penup()
            new_brick.color(random.choice(COLORS))
            x_cor = column * 75

            x_tobe = x_cor -345
            y_tobe = y_cor + 160

            new_brick.goto(x_tobe, y_tobe)

            all_bricks_list.append(new_brick)

create_bricks()

# Initialize scoreboard and ball
scoreboard = Scoreboard()
ball = Ball()

# Allow keys to be pressed and work
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "a")
screen.onkeypress(paddle.go_right, "d")

# Start Game
game_is_on = True

while game_is_on:
    # Ball speed
    time.sleep(0.01)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    #Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -220:
        ball.bounce_y()

    #Detect paddle misses
    if ball.ycor() < -280:
        # uncomment if you want to continuously play
        # ball.reset_position()
        scoreboard.game_over()

    # detect collision with bricks
    if not len(all_bricks_list) == 0:
        for i in all_bricks_list:
                if i.ycor()-20 <= ball.ycor() <= i.ycor()+20 and (i.xcor()-60 < ball.xcor()<i.xcor()+60):
                    i.goto(1000,1000)
                    ball.bounce_y()
                    all_bricks_list.remove(i)
                    scoreboard.inc_score()
    # Check to see if player has won
    else:
        scoreboard.winner()
        game_is_on = False


screen.exitonclick()
