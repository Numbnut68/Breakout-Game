from turtle import Turtle

SCORE_FONT = ("Courier", 24, "normal")
GO_FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-220, 265)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"SCORE: {self.score}", align="center", font=SCORE_FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GO_FONT)

    def winner(self):
        self.goto(0, 0)
        self.write("WINNER WINNER", align="center", font=GO_FONT)    