from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
NUM_OF_ROWS = 4
NUM_OF_BRICKS = 10

class BrickManager:

    def __init__(self):
         self.all_bricks_list = []
         self.total_bricks = (NUM_OF_BRICKS * NUM_OF_ROWS) -1

    def create_bricks(self):
        for row in range(NUM_OF_ROWS):
            y_cor = row * 30
            for column in range(NUM_OF_BRICKS):
                new_brick = Turtle("square")
                new_brick.shapesize(stretch_len=3, stretch_wid=1)
                new_brick.penup()
                new_brick.color(random.choice(COLORS))
                x_cor = column * 75

                x_tobe = x_cor -345
                y_tobe = y_cor + 160
                coords = [x_tobe, y_tobe]

                new_brick.goto(x_tobe, y_tobe)

                self.all_bricks_list.append(new_brick)
