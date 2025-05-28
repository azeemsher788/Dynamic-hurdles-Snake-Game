from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(150, 220)
        self.color("#FFC913")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align="center", font=("Poppins", 20, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def mega_score(self):
        self.clear()
        self.score += 10
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("Red")
        self.write(arg="Game Over", align="center", font=("Poppins", 40, "normal"))

    def highest_score(self, highest):
        score = Turtle()
        score.color("#0fff03")
        score.penup()
        score.hideturtle()
        score.goto(150, -260)
        score.write(arg=f"Highest Score: {highest}", align="center", font=("Roboto", 20, "bold"))
