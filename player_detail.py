from turtle import Turtle, Screen


class Timer(Turtle):

    def __init__(self):
        super().__init__()
        self.time = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 340)

    def increase_time(self):
        self.time += 1
        self.game_time()

    def game_time(self):
        self.clear()
        sec = (self.time//10) % 60
        minute = (self.time//10)//60
        if sec < 10:
            sec = f"0{sec}"
        if minute < 10:
            minute = f"0{minute}"
        self.color("Blue")
        self.write(arg=f"Time [ {minute} : {sec} ]", align="center", font=("Arial", 17, "bold"))


class Player(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        self.name = screen.textinput(title="Player Name", prompt="Enter your name.")
        self.health = 500
        # inherit from Turtle class
        self.hideturtle()
        self.penup()
        self.color("#FFC913")
        self.goto(-150, 220)
        self.player_name()
        self.player_health()

    def player_name(self):
        # To print player name on screen
        player_name = Turtle()
        player_name.hideturtle()
        player_name.penup()
        player_name.color("#0fff03")
        player_name.goto(-150, -260)
        player_name.write(arg=f"Player: {self.name}", align="center", font=("Roboto", 20, "bold"))

    def increase_health(self):
        self.health += 15
        self.player_health()
    def reduce_health(self):
        self.health -= 1
        self.player_health()

    def health_zero(self):
        if self.health//5 == 0:
            return True
        return False

    def player_health(self):
        self.clear()
        self.write(arg=f"Health: {self.health//5}", align="center", font=("Poppins", 20, "normal"))
