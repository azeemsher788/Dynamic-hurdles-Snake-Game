import time
from random import randint
from turtle import Turtle


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.start_time = time.time()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("Blue")
        self.speed("fastest")
        self.food_digest = 0
        self.new_food()

    def new_food(self):
        random_x = randint(-580, 580)
        random_y = randint(-320, 320)
        self.goto(random_x, random_y)
        # Generate mega_food after every five eating
        if self.food_digest % 5 == 0 and self.food_digest != 0:
            self.mega_food_fun()
        self.food_digest += 1   # To count eating

    def mega_food_fun(self):
        mega_food = Turtle()
        mega_food.shape("square")
        mega_food.penup()
        mega_food.speed("fastest")
        mega_food.shapesize(0.9)
        mega_food.color("#00DC07")
        random_x = randint(-580, 280)
        random_y = randint(-320, 320)
        mega_food.goto(random_x, random_y)
        # Assigning every mega_food object as previous so to hide it from anywhere
        self.previous_mega_food = mega_food
        self.start_time = time.localtime().tm_sec

    def hide_mega_food(self):
        self.previous_mega_food.hideturtle()

    def mega_food_counter(self):
        """To count so that mega_food hide after every 15 sec"""
        delay = 15
        elapsed_time = time.localtime().tm_sec - self.start_time
        if elapsed_time == delay:
            self.hide_mega_food()
